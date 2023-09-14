from banjo.urls import route_get, route_post
from banjo.http import BadRequest
from .models import Fortune

@route_post('fortune_teller/new',args={'fortune_statement':str, 'category_school': bool, 'category_general': bool})
def new_fortune(params):
    fortune = Fortune.from_dict(params)
    fortune.save()

    return  {'fortune': fortune.to_dict()}

@route_get('fortune_teller/all')
def all_fortunes(params):
    fortunes_list = []

    for fortune in Fortune.objects.all():
        fortunes_list.append(fortune.to_dict())

    return {'fortunes':fortunes_list}

@route_post('fortune_teller/edit',args={'id':int,'updated_statement':str})
def edit_fortune(params):

    fortune = Fortune.objects.get(id=params['id'])
    fortune.change_statement(params['updated_statement'])


    return {'fortune': fortune.to_dict()}

@route_post('fortune_teller/like',args={'id':int})
def like_fortune(params):

    fortune = Fortune.objects.get(id=params['id'])
    fortune.increase_likes()

    return  {'fortune': fortune.to_dict()}


@route_post('fortune_teller/dislike',args={'id':int})
def dislike_fortune(params):

    fortune = Fortune.objects.get(id=params['id'])
    fortune.increase_dislikes()

    return  {'fortune': fortune.to_dict()}



@route_get('fortune_teller/random')
def random(params):
    fortune = Fortune.objects.order_by('?').first()

    return  {'fortune': fortune.to_dict()}
