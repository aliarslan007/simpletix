from django.shortcuts import render, redirect
from .forms import EventForm
from .models import Event, EventType,EventCategory, EventSubcategory, NewEvent, Ticket, TicketType
from datetime import datetime

def createTicketType(request):
    if TicketType.objects.count() == 0:
        dummy_data = ['Paid', 'Donation', 'Free']
        for data in dummy_data:
            ticket_type = TicketType()
            ticket_type.name = data
            # Set values for other EventType fields
            ticket_type.save()
    # ticketTypes=TicketType.objects.all()
    # for ticketType in ticketTypes:
    #     print("ticket name is : "+str(ticketType.name))


def createEventType(request):
    if EventType.objects.count() == 0:
        dummy_data = ['Singing', 'Dancing', 'Circus','Others']
        for data in dummy_data:
            event_type = EventType()
            event_type.name = data
            # Set values for other EventType fields
            event_type.save()
    # eventTypes=EventType.objects.all()
    # for eventType in eventTypes:
    #     print("event name is : "+str(eventType.name))

def createEventCategory(request):
    if EventCategory.objects.count() == 0:
        dummy_data = ['Art', 'IT', 'Entertainmen']
        for data in dummy_data:
            event_category = EventCategory()
            event_category.name = data
            # Set values for other EventType fields
            event_category.save()
    # eventCategories=EventCategory.objects.all()
    # for eventCategory in eventCategories:
    #     print("event name is : "+str(eventCategory.name))

def createEventSubCategory(request):
    if EventSubcategory.objects.count() == 0:
        dummy_data = ['fashion', 'concert', 'Entertainmen']
        for data in dummy_data:
            event_subcategory = EventSubcategory()
            event_subcategory.name = data
            # Set values for other EventType fields
            event_subcategory.save()

def home(request):
    createTicketType(request)
    createEventType(request)
    createEventCategory(request)
    createEventSubCategory(request)
    if request.method == 'POST':
        # Access the form data here
        event_type_name = str(request.POST.get('event_type')).lower()
        event_type_name = event_type_name.strip("('),")
        event_catergory_name =str(request.POST.get('event_category')).lower()
        event_subcatergory_name =request.POST.get('event_subcategory')
        event_type = EventType.objects.get(name__iexact=event_type_name)
        event_category = EventCategory.objects.get(name__iexact=event_catergory_name)
        event_subcategory = EventSubcategory.objects.get(name__iexact=event_subcatergory_name)
        ticket_type_name= str(request.POST.get('ticket_type')).lower()
        print("tickt type is "+str(ticket_type_name))
        ticket_type_name = ticket_type_name.strip("('),")
        print("tickt type after is "+str(ticket_type_name))
        ticket_type = TicketType.objects.get(name__iexact=ticket_type_name)
        event = NewEvent.objects.create(
            # Set the values for Event fields based on form data
            Event_Name = request.POST.get('Event_Name'),
            event_type = event_type,
            event_category = event_category,
            event_subcategory = event_subcategory,
            Venue_name = request.POST.get('Venue_name'),
            Event_description = request.POST.get('Event_description'),
            Event_image = request.FILES.get('Event_image'),
            start_date = request.POST.get('start_date'),
            start_time = request.POST.get('start_time'),
            end_date = request.POST.get('end_date'),
            end_time = request.POST.get('end_time'),
            total_capacity_of_event = request.POST.get('total_capacity_of_event'),
            # event.Ticket. = request.POST.get('Event_Name')
            # event_name = request.POST.get('Event_Name')
            # event_name = request.POST.get('Event_Name')
            # event_name = request.POST.get('Event_Name')
            # Other Event fields...
            
        )
        ticket= Ticket.objects.create(
            event=event,
            ticket_type=ticket_type,
            ticket_name = request.POST.get('ticket_name') if request.POST.get('ticket_name') is not None else "",
            ticket_quantities = int(request.POST.get('ticket_quantities')) if request.POST.get('ticket_quantities') is not None else 0,
            ticket_price = float(request.POST.get('ticket_price')) if request.POST.get('ticket_price') is not None else 0.0
        )
        if event:
            print("after creating event")
            print("after creating event and its id is "+str(event.id))
            print(event)
        else:
            print("after creating event and it is none")
        # Process the form data or perform any necessary actions
        # ...
        return redirect('event_detail_all' )
    else:
        ticketTypes=TicketType.objects.all()
        eventTypes=EventType.objects.all()
        eventCategories=EventCategory.objects.all()
        eventSubCategories=EventSubcategory.objects.all()
        context={'ticketTypes':ticketTypes, 'eventTypes':eventTypes,'eventCategories':eventCategories,'eventSubCategories':eventSubCategories}
    return render(request, 'myevent/index.html',context)

def create_event_step1(request):
    print("in step 1 start ")
    if request.method == 'POST':
        print("in step 1 first if ")
        form = EventForm(request.POST)
        # print(form)
        if form.is_valid():
            
            print("in step 1 2nd if ")
            step1_data = {
                'title': form.cleaned_data['title'],
                'description': form.cleaned_data['description'],
                'date': form.cleaned_data['date'].strftime('%Y-%m-%d'),
                'time': form.cleaned_data['time'].isoformat(),
            }
            request.session['step1_data'] = step1_data

            return redirect('create_event_step2')
        else:
            print(form.errors)
    else:
        form = EventForm()
        print("in step 1 first else ")
   
    return render(request, 'myevent/create_event_step1.html', {'form': form})

def create_event_step2(request):
    step1_data = request.session.get('step1_data')
    if step1_data is None:
        return redirect('create_event_step1')
    print("in step2  before POST")
    if request.method == 'POST':
        print("in step2  after  POST")
        # form = EventForm(request.POST, initial=step1_data)
        # form = EventForm(initial=step1_data)
        # form.data = form.data.copy() 
        # print(" step 1 form ")
        # print(form)
        
        form = EventForm(initial=step1_data) 
        print(" step 1 form ")
        print(form)
        form.data = form.data.copy()
        form.data.update(request.POST)
        # form.data = FormData(request.POST)
        # form.data.update(request.POST)
        form.is_bound = True
        print(" step 2+ form ")
        print(form)

        if form.is_valid():
            
            location = request.POST.get('location')
            ticket_price = request.POST.get('ticket_price')
            print("in step2  inside valid")
             # Process complete form
            form.instance.date = datetime.strptime(step1_data['date'], '%Y-%m-%d').date()
            event = form.save(commit=False)
            
            print(" befor event object , price "+str(event.ticket_price))
            

            newEvent = Event.objects.create(
            title=step1_data['title'],
            description=step1_data['description'],
            date=step1_data['date'],
            time=step1_data['time'],
            location=location,
            ticket_price=ticket_price
        )
            print(str(newEvent.title))
            print(str(newEvent.description))
            print(str(newEvent.date))
            print(str(newEvent.time))
            print(str(newEvent.location))
            print(str(newEvent.ticket_price))
            newEvent.save()
            del request.session['step1_data']
            return redirect('event_detail', event_id=newEvent.id)
        else:
            print(form.errors)
    else:
        print("in else of step 2")
        form = EventForm(initial=step1_data)
   
    return render(request, 'myevent/create_event_step2.html', {'form': form})

def event_detail(request, event_id):
    # event = NewEvent.objects.get(pk=event_id)
    events = NewEvent.objects.all()

    return render(request, 'myevent/event_detail.html', {'events': events})


def event_detail_all(request):
    # event = NewEvent.objects.get(pk=event_id)
    events = NewEvent.objects.all()
    tickets = Ticket.objects.all()
    context = {'events': events, 'tickets': tickets}
    print("length of events are ")
    print(str(len(events)))

    return render(request, 'myevent/event_detail_all.html', context)
