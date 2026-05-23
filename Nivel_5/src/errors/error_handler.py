from src.views.http_types.http_response import HttpResponse
from .error_types.http_bad_request import HttpBadRequestError

def handle_errors(error: Exception) -> HttpResponse:
  if isinstance(error, HttpBadRequestError) :
    return HttpResponse(
      status_code=error.status_code,
      body={
        "errors": [{
          "title": error. name,
          "detail": error.message
        }]
      }
    )
