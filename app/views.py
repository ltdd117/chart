from typing import Any
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request

class ChartView(APIView):
    def __init__(self):
        super().__init__()
       
        self.chuoi_1 = [0.382, 0.236, 0.146]
        self.chuoi_2 = [0.146, 0.09, 0.055]
  
        self.x = 257
        self.y = 730

    def post(self, request: Request): 
        point1 = request.data.get('point1', 0)  
        point2 = request.data.get('point2', 0)
        point3 = request.data.get('point3', 0)

        if not self.is_valid_input(point1, point2, point3):
            return Response({'error': 'Invalid input. Points must be numeric.'})

        result = self.check_long_short(point1, point2, point3)
        return Response({'result': result})

    def is_valid_input(self, *points: Any) -> bool:
        try:
            for point in points:
                float(point)  # Try converting to float
            return True
        except (ValueError, TypeError):
            return False

    def check_long_short(self, point1, point2, point3):
        try:
            point1 = float(point1)
            point2 = float(point2)
            point3 = float(point3)
        except (ValueError, TypeError):
            return Response({'error': 'Invalid input. Points must be numeric.'})

        if point1 < point3 < point2:  
            thlong_1 = [(point2 - point1 + point1 * i) / i for i in self.chuoi_1]
            thlong_2 = [(point1 * (i - 1) + point3) / i for i in self.chuoi_2]
            truonghop = 'LONG'
            return {'Truong hop': truonghop, 'Cong thuc 1': thlong_1, 'Cong thuc 2': thlong_2}
        else:
            thshort_1 = [(point2 - point1 + point1 * i) / i if i != 0 else float('inf') for i in self.chuoi_1]
            thshort_2 = [(point3 + point1 * (i - 1)) / i for i in self.chuoi_2]
            truonghop = 'SHORT'
            return {'Truong hop': truonghop, 'Cong thuc 1': thshort_1, 'Cong thuc 2': thshort_2}
