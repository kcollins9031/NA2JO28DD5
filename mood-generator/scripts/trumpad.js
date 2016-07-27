// Mouseover/ Click sound effect- by JavaScript Kit (www.javascriptkit.com)
// Visit JavaScript Kit at http://www.javascriptkit.com/ for full source code

//** Usage: Instantiate script by calling: var uniquevar=createsoundbite("soundfile1", "fallbackfile2", "fallebacksound3", etc)
//** Call: uniquevar.playclip() to play sound

var html5_audiotypes={ //define list of audio file extensions and their associated audio types. Add to it if your specified audio file isn't on this list:
  // "mp3": "audio/mpeg",
  // "mp4": "audio/mp4",
  // "ogg": "audio/ogg",
  "wav": "audio/wav"
}

function createsoundbite(sound)
{
  var html5audio=document.createElement('audio')
  if (html5audio.canPlayType){ //check support for HTML5 audio
    for (var i=0; i<arguments.length; i++){
      var sourceel=document.createElement('source')
      sourceel.setAttribute('src', arguments[i])
      if (arguments[i].match(/\.(\w+)$/i))
        sourceel.setAttribute('type', html5_audiotypes[RegExp.$1])
      html5audio.appendChild(sourceel)
    }
    html5audio.load()
    html5audio.playclip=function(){
      html5audio.pause()
      html5audio.currentTime=0
      html5audio.play()
    }
    return html5audio
  }
  else{
    return {playclip:function(){throw new Error("Your browser doesn't support HTML5 audio unfortunately")}}
  }
}

/* this function opens the loop selection list in a drop down menu */
function loop_list()
{
  document.getElementById("dropdown_menu").classList.toggle("show");
}

/* when the user clicks outside the list, this function closes the list */
window.onclick = function(event) {
  if (!event.target.matches('.dropbtn')) {

    var dropdowns = document.getElementsByClassName("dropdown_content");
    var i;
    for (i = 0; i < dropdowns.length; i++) {
      var openDropdown = dropdowns[i];
      if (openDropdown.classList.contains('show')) {
        openDropdown.classList.remove('show');
      }
    }
  }
}

//Initialize two sound clips with 1 fallback file each:

//var mouseoversound=createsoundbite("whistle.ogg", "whistle.mp3")

var pad1=createsoundbite("/drum_kit/bingbing.wav")
var pad2=createsoundbite("/drum_kit/bingbing2.wav")
var pad3=createsoundbite("/drum_kit/bum.wav")
var pad4=createsoundbite("/drum_kit/bongbong.wav")
var pad5=createsoundbite("/drum_kit/clink.wav")
var pad6=createsoundbite("/drum_kit/bababababa.wav")
