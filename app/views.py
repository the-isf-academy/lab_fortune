from banjo.urls import route_get, route_post
from banjo.http import BadRequest
from .models import Prediction


@route_get('magic8/all')
def predictions_all(params):
    predictions_list = []

    for prediction in Prediction.objects.all():
        predictions_list.append(prediction.to_dict())

    return {'predictions':predictions_list}

@route_post('magic8/edit',args={'id':int,'updated_statement':str})
def edit(params):
    if 'id' not in params or 'updated_statement' not in params:
        raise BadRequest('incorrect request')

    updated_statement = params['updated_statement']
    id = params['id']
    prediction = Prediction.objects.get(id=id)

    prediction.statement = updated_statement
    prediction.reset_ratings()
    prediction.save()

    return prediction.to_dict()

@route_post('magic8/rate',args={'id':int,'approve':bool})
def edit(params):
    if 'id' not in params or 'approve' not in params:
        raise BadRequest('incorrect request')

    approve = params['approve']
    id = params['id']
    prediction = Prediction.objects.get(id=id)
    if approve:
        prediction.liked()
    else:
        prediction.disliked()

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
