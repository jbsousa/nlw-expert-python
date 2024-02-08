from src.views.http_types.http_request import HttpRequest
from src.views.http_types.http_response import HttpResponse

class TagCreatorView:
    '''
        responsability for interating with HTTP
    '''

    def validate_and_create(self, http_request: HttpRequest) -> HttpResponse:
        #body = http_request.body
        #product_code = body["product_code"]

        # lógica de tegra de negócio
        print("Estou na minha view")
        print(http_request)
        # retorno http
        return HttpResponse(status_code=200, body={"hello": "world"})
