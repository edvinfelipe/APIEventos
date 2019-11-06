from rest_framework.pagination import LimitOffsetPagination

class ViewPagination1(LimitOffsetPagination):
    default_limit= 20
    max_limit= 100