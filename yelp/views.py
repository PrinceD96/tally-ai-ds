# coding: utf-8
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from rest_framework import generics
from .models import YelpYelpScraping
from .serializers import YelpYelpScrapingSerializer
from tallylib.scraper import yelpScraper
from tallylib.textrank import yelpTrendyPhrases
from tallylib.reviewfrequency import getReviewFrequencyResults
from tallylib.scattertext import getYelpWordsReviewFreq, getYelp3Words
from tallylib.no_nlp_long_phrases import getYelpPhrases

import requests
import json


def hello(request):
    result = "Hello, you are at the Tally Yelp Analytics home page."
    return HttpResponse(result)

def home(request, business_id):
    result = "This is Yelp Analytics home page."
    viztype = request.GET.get('viztype')
    if viztype == '0':
        result = json.dumps(getYelpWordsReviewFreq(business_id))
    elif viztype == '1':
        pass
    elif viztype == '2':
        pass
    else:
        result = json.dumps(yelpScraper(business_id))
    return HttpResponse(result)


class YelpYelpScrapingCreateView(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = YelpYelpScraping.objects.all()
    serializer_class = YelpYelpScrapingSerializer

    def perform_create(self, serializer):
        """Save the post data when creating a new bucketlist."""
        serializer.save()


class YelpYelpScrapingDetailsView(generics.RetrieveUpdateDestroyAPIView):
    """This class handles the http GET, PUT and DELETE requests."""
    queryset = YelpYelpScraping.objects.all()
    serializer_class = YelpYelpScrapingSerializer


