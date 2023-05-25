# Copyright 2015 gRPC authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""The Python implementation of the GRPC helloworld.Greeter server."""
import logging
import statistics
from concurrent import futures
from datetime import date, datetime

from employee_pb2 import *
from employee_pb2_grpc import *


class EmployeeService(EmployeeStubServicer):
    employees = []
    ages = []

    def GetMedianAge(self, request, context):
        return MedianAgeResponse(Age=int(statistics.median(self.ages)))

    def AddEmployee(self, request: EmployeeCreationRequest, context):
        self.handle_create_employee_req(request)
        return EmployeeCreationResponse(id=len(self.employees))

    def SendMessage(self, request, context):
        return MessageResponse(text=f'{request.text} was handled')

    def CreateEmployeeAsStreamAndGetMedianAge(self, request_iterator, context):
        for req in request_iterator:
            self.handle_create_employee_req(req)

        return MedianAgeResponse(Age=int(statistics.median(self.ages)))

    def CreateEmployeeAsStreamAndGetMedianAgeAsStream(self, request_iterator, context):
        for req in request_iterator:
            self.handle_create_employee_req(req)
            yield MedianAgeResponse(Age=int(statistics.median(self.ages)))

    def handle_create_employee_req(self, employee):
        self.employees.append(employee)
        if employee.birthday:
            today = date.today()
            birthday = datetime.strptime(employee.birthday, '%Y-%m-%d')
            age = int(today.year - birthday.year)
            self.ages.append(age)


def serve():
    port = '5000'
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=1))
    add_EmployeeStubServicer_to_server(EmployeeService(), server)
    server.add_insecure_port('[::]:' + port)
    server.start()
    print("Server started, listening on " + port)
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    serve()
