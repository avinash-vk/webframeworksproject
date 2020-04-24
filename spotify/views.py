from django.shortcuts import render
from .models import Playlist
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
import json
import requests
import sys
import spotipy
import spotipy.util as util
from django.shortcuts import render, get_object_or_404
from django.shortcuts import render,redirect,HttpResponseRedirect
client_id='c0d2821e26fd468db7d04420ef7e0554'
client_secret='cf5d6bfebe414d659eaefebf54e79682'
scope = 'playlist-modify-public'
redirect_uri='http://127.0.0.1:8000/'
username="xxxxxx"
api_url_base = 'https://api.spotify.com/v1/playlists/'
def add_playlist(request):
    api_token = util.prompt_for_user_token(username, scope,client_id,client_secret,redirect_uri)
    new_playlist = None
    if request.method == 'POST':
        linkvar=request.POST.get('messages')
        new_playlist=Playlist(link=linkvar)
        l=linkvar.split('/')[4].split('?')[0]
        new_playlist.playlist_id=l
        if api_token:
            headers = {'Content-Type': 'application/json',
                   'Authorization': 'Bearer {0}'.format(api_token)}
            api_url = api_url_base+l
            response = requests.get(api_url, headers=headers)
            if response.status_code == 200:
                playlist=json.loads(response.content.decode('utf-8'))
                new_playlist.owner_id=playlist['owner']['id']
                new_playlist.name=playlist['name']
                new_playlist.cover_url=playlist['images'][0]['url']
        new_playlist.author = request.user
        new_playlist.save()
    return redirect('dashboard')
def save_library(request,playlist_id):
    username = "1qvw6ha3tuv6icx9k78c7g5d3"
    playlist=get_object_or_404(Playlist, playlist_id=playlist_id)
    token = util.prompt_for_user_token(username, scope,client_id,client_secret,redirect_uri)
    if token:
        sp = spotipy.Spotify(auth=token)
        sp.user_playlist_follow_playlist(playlist.owner_id,playlist.playlist_id)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
