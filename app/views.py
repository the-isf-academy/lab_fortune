from banjo.urls import route_get, route_post
from .models import Fortune

@route_post('fortune/new', args={'fortune_statement':str, 'category_happy': bool, 'category_sad': bool})
def new_fortune(params):
    fortune = Fortune.from_dict(params)

    fortune.save()

    return  {'fortune': fortune.to_dict()}


@route_get('fortune/all')
def all_fortunes(params):
    fortunes_list = []

    for fortune in Fortune.objects.all():
        fortunes_list.append(fortune.to_dict())

    return {'fortunes':fortunes_list}

@route_post('fortune/edit',args={'id':int,'updated_statement':str})
def edit_fortune(params):

    fortune = Fortune.objects.get(id=params['id'])
    fortune.change_statement(params['updated_statement'])

    return {'fortune updated': fortune.to_dict()}


@route_post('fortune/like',args={'id':int})
def like_fortune(params):
    fortune = Fortune.objects.get(id=params['id'])
    fortune.increase_likes()

    return  {'fortune': fortune.to_dict()}

@route_get('fortune/random', args={'category_happy': bool, 'category_sad': bool})
def random(params):
    payload_category_happy = params['category_happy']
    payload_category_sad = params['category_sad']

    fortunes_filtered = Fortune.objects.filter(category_happy=payload_category_happy).filter(category_sad=payload_category_sad)
    random_fortune = fortunes_filtered.order_by('?').first()
    
    return  {'random fortune': random_fortune.to_dict()}
