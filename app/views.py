from banjo.urls import route_get, route_post
from banjo.http import BadRequest
from .models import Prediction


@route_get('magic8/all')
def riddles_all(params):
    predictions_list = []

    for prediction in Prediction.objects.all():
        predictions_list.append(prediction.to_dict())

    return {'predictions':predictions_list}

@route_post('magic8/edit',args={'id':int,'update':str})
def edit(params):
    if 'id' not in params or 'update' not in params:
        raise BadRequest('incorrect request')

    updated_statement = params['update']
    id = params['id']
    prediction = Prediction.objects.get(id=id)

    prediction.statement = updated_statement
    prediction.save()

    return prediction.to_dict()

@route_post('magic8/new',args={'statement':str})
def edit(params):
    if 'statement' not in params:
        raise BadRequest('incorrect request')

    statement = params['statement']
    prediction = Prediction.from_dict(params)
    prediction.save()
    return prediction.to_dict()

@route_get('magic8/random')
def random(params):
    prediction = Prediction.objects.order_by('?').first()

    return prediction.to_dict()
