from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render, get_object_or_404
from django.template import RequestContext

from django.urls import reverse

from django.db import connection

from website.models import Product, Status

from website.forms import UserForm, ProductForm


def index(request):
    template_name = 'website/index.html'
    return render(request, template_name, {})


# Create your views here.
def register(request):
    '''Handles the creation of a new user for authentication

    Method arguments:
      request -- The full HTTP request object
    '''

    # A boolean value for telling the template whether the registration was successful.
    # Set to False initially. Code changes value to True when registration succeeds.
    registered = False

    # Create a new user by invoking the `create_user` helper method
    # on Django's built-in User model
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)

        if user_form.is_valid():
            # Save the user's form data to the database.
            user = user_form.save()

            # Now we hash the password with the set_password method.
            # Once hashed, we can update the user object.
            user.set_password(user.password)
            user.save()

            # Update our variable to tell the template registration was successful.
            registered = True

        return login_user(request)

    elif request.method == 'GET':
        user_form = UserForm()
        template_name = 'website/register.html'
        return render(request, template_name, {'user_form': user_form})


def login_user(request):
    '''Handles the creation of a new user for authentication

    Method arguments:
      request -- The full HTTP request object
    '''

    # Obtain the context for the user's request.
    context = RequestContext(request)

    # If the request is a HTTP POST, try to pull out the relevant information.
    if request.method == 'POST':

        # Use the built-in authenticate method to verify
        username=request.POST['username']
        password=request.POST['password']
        authenticated_user = authenticate(username=username, password=password)

        # If authentication was successful, log the user in
        if authenticated_user is not None:
            login(request=request, user=authenticated_user)
            return HttpResponseRedirect('/')

        else:
            # Bad login details were provided. So we can't log the user in.
            print("Invalid login details: {}, {}".format(username, password))
            return HttpResponse("Invalid login details supplied.")


    return render(request, 'website/login.html', {}, context)

# Use the login_required() decorator to ensure only those logged in can access the view.
@login_required
def user_logout(request):
    # Since we know the user is logged in, we can now just log them out.
    logout(request)

    # Take the user back to the homepage. Is there a way to not hard code
    # in the URL in redirects?????
    return HttpResponseRedirect('/')

def overview(request):
    billing = Product.objects.filter(status_id=1)
    design = Product.objects.filter(status_id=2)
    cnc = Product.objects.filter(status_id=3)
    grinding = Product.objects.filter(status_id=4)
    painting = Product.objects.filter(status_id=5)
    packaging = Product.objects.filter(status_id=6)
    shipping = Product.objects.filter(status_id=7)
    product = Product.objects.all()
    template_name = 'website/overview.html'
    context = {'billing': billing, 'design': design,'cnc':cnc,'grinding':grinding,'painting':painting,'packaging':packaging,'shipping':shipping,'products':product, 'percentage': 100}
    return render(request, template_name, context)

def billing_status(request):
    billing = Product.objects.filter(status_id=1)
    product = Product.objects.filter(status_id=1)
    template_name = 'website/billing.html'
    print(product)
    context = {'billing': billing, 'products': product, "percentage": 20}
    return render(request, template_name, context)

def design_status(request):
    design = Product.objects.filter(status_id=2)
    product = Product.objects.filter(status_id=2)
    template_name = 'website/design.html'
    print(product)
    context = {'design': design, 'products': product, "percentage": 30}
    return render(request, template_name, context)

def cnc_status(request):
    cnc = Product.objects.filter(status_id=3)
    product = Product.objects.filter(status_id=3)
    template_name = 'website/CNC.html'
    print(product)
    context = {'cnc': cnc, 'products': product, "percentage": 40}
    return render(request, template_name, context)

def grinding_status(request):
    grinding = Product.objects.filter(status_id=4)
    product = Product.objects.filter(status_id=4)
    template_name = 'website/grinding.html'
    print(product)
    context = {'grinding': grinding, 'products': product, "percentage": 60}
    return render(request, template_name, context)

def painting_status(request):
    painting = Product.objects.filter(status_id=5)
    product = Product.objects.filter(status_id=5)
    template_name = 'website/painting.html'
    print(product)
    context = {'painting': painting, 'products': product, "percentage": 70}
    return render(request, template_name, context)

def packaging_status(request):
    packaging = Product.objects.filter(status_id=6)
    product = Product.objects.filter(status_id=6)
    template_name = 'website/packaging.html'
    print(product)
    context = {'packaging': packaging, 'products': product, "percentage": 90}
    return render(request, template_name, context)

def shipping_status(request):
    shipping = Product.objects.filter(status_id=7)
    product = Product.objects.filter(status_id=7)
    template_name = 'website/shipping.html'
    print(product)
    context = {'shipping': shipping, 'products': product, "percentage": 100}
    return render(request, template_name, context)

def process_product(request):
    if request.method == 'GET':
        product_form = ProductForm()
        template_name = 'website/process.html'
        return render(request, template_name, {'product_form': product_form})

    if request.method == "POST":
        upc = request.POST["UPC"] 
        description = request.POST["description"]
        business = 1
        status = 1

        with connection.cursor() as cursor:
            cursor.execute("INSERT into website_product VALUES(%s, %s, %s, %s, %s)", [None, upc, description, business, status])

    return HttpResponseRedirect(reverse('website:overview'))



