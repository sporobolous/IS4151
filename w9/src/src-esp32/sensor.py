from flask import make_response, abort



def create(temperature):

    print('********** temperature ' + str(temperature))
    
    return make_response({'temperature':temperature}, 200)