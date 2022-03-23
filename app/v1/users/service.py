from app.v1.users.coordinator import Coordinator
from collections import OrderedDict
class SubApp1Service:

    def __init__(self, params, headers):
        self.params = params
        self.headers = headers
        self.coordinator=Coordinator()

    def get_static_api_response(self):
        data=self.params
        age=int(data['age'])
        if age>=18:
            data['canvote']='yes'
        else:
            data['canvote']='no'
        return data,'success'

    def get_static_api_response1(self):
        data=self.params
        age=int(data['age'])
        if age>=18:
            data['canvote']='yes'
        else:
            data['canvote']='no'
        return data,'success'

    def get_static_api_response2(self):
        customer_id=self.params.get('customer_id')
        customer_details=self.coordinator.get_customer_detail(customer_id)
        response={'customer_id':customer_id,'quotes':customer_details}
        dic=OrderedDict(reversed(list(response.items())))
        return dic,'success'











        # if customer_details['is_active'] or customer_details['quote_id']:
        #     dic=customer_details['is_active'],customer_details['quote_id']
        # return dic,'success'
        # if customer_details:
        #     customer_details=customer_details['quote_id']

            # quotes1=customer_details.get('is_active')
            # quotes2=customer_details.get('quote_id')
            # quotes=[]
            # quotes.append(quotes2)
            # quotes.append(quotes1)
        # customer_details['quotes']=quotes
        