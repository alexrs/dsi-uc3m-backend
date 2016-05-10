
  // 2. This code loads the IFrame Player API code asynchronously.
  var tag = document.createElement('script');

  tag.src = "https://www.youtube.com/iframe_api";
  var firstScriptTag = document.getElementsByTagName('script')[0];
  firstScriptTag.parentNode.insertBefore(tag, firstScriptTag);

  // 3. This function creates an <iframe> (and YouTube player)
  //    after the API code downloads.
  var player;
  function onYouTubeIframeAPIReady() {
    id = document.getElementById("player").innerHTML.trim()

    if (!id || id == "None"){
      id = "YytwyEtBL6Y";
    }

    player = new YT.Player('player', {
      showinfo: '0',
      width: '100%',
      height: '300',
      controls: '0',
      color: 'red',
      autohide: '1',
      fs: '1',
      videoId: id,
      events: {
        'onReady': onPlayerReady,
        'onStateChange': onPlayerStateChange
      }
    });
  }

  // 4. The API will call this function when the video player is ready.
  function onPlayerReady(event) {
    //event.target.playVideo();
  }

  // 5. The API calls this function when the player's state changes.
  //    The function indicates that when playing a video (state=1),
  //    the player should play for six seconds and then stop.
  var static = false;
  var nav = document.getElementById("navbar-top");
  function onPlayerStateChange(event) {
    if (event.data == YT.PlayerState.PLAYING) {
        nav.style.display = "none";
    } else {
        nav.style.display = "block";
    }
  }

  function loadVideo(videoID) {
    if (player) { player.loadVideoById(videoID);}
  }
