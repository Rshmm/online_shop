def get_form_set_key(request):
    form_set_key = [k for k in request.POST  if k.startswith('form-')]
    unique_indexes = list({k.split('-')[1] for k in form_set_key})
    unique_indexes.sort()
    return unique_indexes

def get_form_set_value(request, key):
    data = request.POST
    prefix = f'form-{key}'
    return {
        'title' : data[f'{prefix}-title'],
        'recipient_full_name' : data[f'{prefix}-recipient_full_name'],
        'state' : data[f'{prefix}-state'],
        'city' : data[f'{prefix}-city'],
        'full_address' : data[f'{prefix}-full_address'],
        'postal_code' : data[f'{prefix}-postal_code'],
        'building_number' : data[f'{prefix}-building_number'],
        'building_unit_number' : data[f'{prefix}-building_unit_number'] 
    }