 kwargs =[{ 
        'name':"ajay",
        'lastname':'kumar'
    },{ 
        'name':"hari",
        'lastname':'haran'
    },{ 
        'name':"vijay",
        'lastname':'thiyagarajan'
    },{ 
        'name':"mushroom",
        'lastname':'thiyagarajan'
    }]
    for k in kwargs:
        for f,l in k.items():
            print(f,l)
            queryset = prem(**k)
            queryset.save()
            #print(queryset)
    # for ind, val in enumerate(queryset):
    #     print(val)