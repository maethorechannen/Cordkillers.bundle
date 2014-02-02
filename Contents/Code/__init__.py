ART      = 'art-default.jpg'
ICON     = 'icon-default.png'

TITLE    = 'Cordkillers'

def Start():

  HTTP.Headers['User-Agent'] = 'PlexCKChannel/0.1'

  ObjectContainer.art = R(ART)
  ObjectContainer.title1 = TITLE

  TrackObject.thumb = R(ICON)

@handler('/video/cordkillers', TITLE, art=ART, thumb=ICON)
def MainMenu():

  oc = ObjectContainer()

  feed = RSS.FeedFromURL('http://feeds.feedburner.com/VideoCordkillersPodcast')

  for item in feed.entries:
    url = item.enclosures[0]['url']
    title = item.title
    summary = item.summary
    originally_available_at = Datetime.ParseDate(item.updated)
    #duration = Datetime.MillisecondsFromString(item.itunes_duration)
    duration = 0    
    oc.add(CreateTrackObject(url=url, title=title, summary=summary, originally_available_at=originally_available_at, duration=duration))
  
  return oc

####################################################################################################
def CreateTrackObject(url, title, summary, originally_available_at, duration, include_container=False):

  container = Container.MP4
  audio_codec = AudioCodec.AAC

  track_object = EpisodeObject(
    key = Callback(CreateTrackObject, url=url, title=title, summary=summary, originally_available_at=originally_available_at, duration=duration, include_container=True),
    rating_key = url,
    title = title,
    summary = summary,
    originally_available_at = originally_available_at,
    #duration = duration,
    items = [
      MediaObject(
        parts = [
          PartObject(key=url)
        ],
        container = container,
        audio_codec = audio_codec,
        audio_channels = 2
      )
    ]
  )

  if include_container:
    return ObjectContainer(objects=[track_object])
  else:
    return track_object

