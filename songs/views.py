from django.shortcuts import render,redirect
from django.views.generic import ListView,TemplateView
from .models import Song,Artist,Rating
from  .forms import SongForm,RatingForm,ArtistForm
from django.core.exceptions import PermissionDenied
# Create your views here.

class SongView(TemplateView):
    template_name='songs/addsong.html'
    
    def get(self,request):
        form= SongForm()
        print("sfs")
        return render(request,self.template_name,{'form': form})

    def post(self,request):

        form=SongForm(request.POST)
        if form.is_valid():
            post=form.save()
            post.user=request.user
            post.save()
            #0text= form.cleaned_data['Name','Date_of_Release','artist'] 
            form = SongForm()
            return redirect('/topsongs/')
        args ={'form': form}
        return render(request,'songs/topsongs.html',args)


class ArtistView(TemplateView):
    template_name='songs/addsartist.html'
    
    def get(self,request):
        form1= ArtistForm()
        print("sfs")
        return render(request,self.template_name,{'form': form1})

    def post(self,request):

        form1=ArtistForm(request.POST)
        if form1.is_valid():
            post=form1.save()
            post.user=request.user
            post.save()
            #0text= form.cleaned_data['Name','Date_of_Release','artist'] 
            form1 = ArtistForm()
            return redirect('/topartist/')
        args ={'form': form1}
        return render(request,'songs/topartist.html',args)



class RatingView(TemplateView):
    template_name = 'songs/rating.html'
    def get(self,request):
        form= SongForm()
        print("sfs")
        return render(request,self.template_name,{'form': form})

    def post(self,request):
        form= RatingForm()
        if form.is_valid():
            Urate=form.save()
            Urate.user=request.user
            Urate.save()
            form= RatingForm()
            return redirect('/topsongs/')
        args={'form':form}
        return render(request,'songs/topsongs.html',args)

def topsongs(request):
    context ={
        'songs': Song.objects.all()
    }
    print(context)
    return render(request,'songs/topsongs.html',context)


def topartist(request):
    context1 ={
        'artists': Artist.objects.all()

    }
    print(context1)
    return render(request,'songs/topartist.html',context1)

def addsong(request):

    return render(request,'songs/addsong.html')

def rating(request):

    return render(request,'songs/rating.html')