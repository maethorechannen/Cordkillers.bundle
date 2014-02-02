Cordkillers.bundle
==================

Plex plugin for the Cordkillers podcast

This is a fairly simple Plex Video Channel pluging for watching the Cordkillers podcast (http://www.cordkillers.com/)

It's based on the Plex Podcast plugin (with some enlightenment about what's going on from shopgirl284's development templates).

Installation
============

Clone the repository and then move Cordkillers.bundle into your Plex plugins directory. Where this is depends on what OS using, for me it's at /var/lib/plexmediaserver/Library/Application\ Support/Plex\ Media\ Server/Plug-ins/

Make sure Cordkillers.bundle is owned by the user plex runs as (for me this is sudo chown plex:plex -R Cordkillers.bundle).

You might need to make sure that Cordkillers.bundle/Content/Code/__init__.py is executable (sudo chmod +x __init__.py)

