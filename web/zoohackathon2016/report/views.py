from rest_framework import viewsets

from report.serializers import ReportSerializer
from report.models import Report


class ReportViewSet(viewsets.ModelViewSet):
    queryset = Report.objects.all()
    serializer_class = ReportSerializer
