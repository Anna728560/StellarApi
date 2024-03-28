from datetime import datetime

from django.db.models import Count, F
from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import extend_schema, OpenApiParameter
from rest_framework import viewsets, mixins
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated

from planetarium.models import (
    AstronomyShow,
    ShowTheme,
    PlanetariumDome,
    ShowSession,
    Reservation,
)
from planetarium.permissions import IsAdminOrIfAuthenticatedReadOnly
from planetarium.serializers import (
    AstronomyShowSerializer,
    AstronomyShowDetailSerializer,
    AstronomyShowListSerializer,

    ShowThemeSerializer,
    ShowSessionListSerializer,

    PlanetariumDomeSerializer,

    ShowSessionSerializer,
    ShowSessionDetailSerializer,

    ReservationSerializer,
    ReservationListSerializer,
)


class AstronomyShowViewSet(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet,
):
    """ViewSet for managing Astronomy Shows."""

    queryset = AstronomyShow.objects.all()
    serializer_class = AstronomyShowSerializer
    permission_classes = (IsAdminOrIfAuthenticatedReadOnly,)

    @staticmethod
    def _params_to_ints(qs):
        """
        Converts a list of string IDs to a list of integers
        """
        return [int(str_id) for str_id in qs.split(",")]

    def get_queryset(self):
        """
        Retrieve the Astronomy Show with filters
        """
        title = self.request.query_params.get("title")
        show_theme = self.request.query_params.get("show_theme")

        queryset = self.queryset

        if title:
            queryset = queryset.filter(title__icontains=title)

        if show_theme:
            show_theme_ids = self._params_to_ints(show_theme)
            queryset = queryset.filter(show_theme__id__in=show_theme_ids)

        return queryset.distinct()

    def get_serializer_class(self):
        """
        Return the appropriate serializer class based on the action.
        """
        if self.action == "list":
            return AstronomyShowListSerializer
        elif self.action == "retrieve":
            return AstronomyShowDetailSerializer
        return AstronomyShowSerializer

    @extend_schema(
        parameters=[
            OpenApiParameter(
                "title",
                type=OpenApiTypes.STR,
                description="Filter AstronomyShow by title "
                            "(ex. ?title=fiction)"
            ),
            OpenApiParameter(
                "show_theme",
                type={"type": "list", "items": {"type": "number"}},
                description="Filter AstronomyShow by show_theme id "
                            "(ex. ?show_theme=1,3)"
            ),
        ]
    )
    def list(self, request, *args, **kwargs):
        """
        List all AstronomyShows.
        """
        return super().list(request, *args, **kwargs)


class ShowThemeViewSet(viewsets.ModelViewSet):
    """Viewset for managing show themes."""

    queryset = ShowTheme.objects.all()
    serializer_class = ShowThemeSerializer
    permission_classes = (IsAdminOrIfAuthenticatedReadOnly,)


class PlanetariumDomeViewSet(viewsets.ModelViewSet):
    """Viewset for managing planetarium domes."""

    queryset = PlanetariumDome.objects.all()
    serializer_class = PlanetariumDomeSerializer
    permission_classes = (IsAdminOrIfAuthenticatedReadOnly,)


class ShowSessionViewSet(viewsets.ModelViewSet):
    """Viewset for managing show sessions."""

    queryset = (
        ShowSession.objects.all()
        .select_related("astronomy_show", "planetarium_dome")
        .annotate(
            tickets_available=(
                    F("planetarium_dome__rows") * F("planetarium_dome__seats_in_row")
                    - Count("tickets")
            )
        )
    )
    serializer_class = ShowSessionSerializer
    permission_classes = (IsAdminOrIfAuthenticatedReadOnly,)

    def get_queryset(self):
        """
        Filter queryset based on query parameters.
        """
        date = self.request.query_params.get("date")
        astronomy_show_id_str = self.request.query_params.get("astronomy_show")

        queryset = self.queryset

        if date:
            date = datetime.strptime(date, "%Y-%m-%d").date()
            queryset = queryset.filter(show_time__date=date)

        if astronomy_show_id_str:
            queryset = queryset.filter(astronomy_show_id=int(astronomy_show_id_str))

        return queryset

    def get_serializer_class(self):
        """
        Return appropriate serializer class based on action.
        """
        if self.action == "list":
            return ShowSessionListSerializer
        if self.action == "retrieve":
            return ShowSessionDetailSerializer
        return ShowSessionSerializer

    @extend_schema(
        parameters=[
            OpenApiParameter(
                "astronomy_show",
                type={"type": "list", "items": {"type": "number"}},
                description="Filter show sessions by astronomy_show id "
                            "(ex. ?astronomy_show=2)"
            ),
            OpenApiParameter(
                "date",
                type=OpenApiTypes.DATE,
                description="Filter show sessions by date "
                            "(ex. ?date=2022-10-23)"
            ),
        ]
    )
    def list(self, request, *args, **kwargs):
        """
        Get list of show sessions.
        """
        return super().list(request, *args, **kwargs)


class ReservationPagination(PageNumberPagination):
    """Pagination class for reservation listings."""

    page_size = 10
    max_page_size = 100


class ReservationViewSet(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    viewsets.GenericViewSet,
):
    """A ViewSet for listing and creating reservations."""

    queryset = Reservation.objects.prefetch_related(
        "tickets__show_session__astronomy_show",
        "tickets__show_session__planetarium_dome",
    )
    serializer_class = ReservationSerializer
    permission_classes = (IsAuthenticated,)
    pagination_class = ReservationPagination

    def get_queryset(self):
        """
        Get the reservations associated with the current user.
        """
        return Reservation.objects.filter(user=self.request.user)

    def get_serializer_class(self):
        """
        Use different serializers based on the action.
        """
        if self.action == "list":
            return ReservationListSerializer

        return ReservationSerializer

    def perform_create(self, serializer):
        """
        Set the user when creating a new reservation.
        """
        serializer.save(user=self.request.user)
