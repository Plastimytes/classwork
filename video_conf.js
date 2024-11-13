const localVideo = document.getElementById('local-video');
const remoteVideo = document.getElementById('remote-video');

navigator.mediaDevices.getUserMedia({ video: true, audio: true })
  .then(stream => {
    localVideo.srcObject = stream;

//Create constant//
    const peerConnection = new RTCPeerConnection();
    stream.getTracks().forEach(track => peerConnection.addTrack(track, stream));

    peerConnection.onicecandidate = event => {
      // Send ICE candidates to the other peer
    };

    peerConnection.ontrack = event => {
      remoteVideo.srcObject = event.streams[0];
    };

    // ... (code to create an offer, send it to the other peer, handle incoming offers, etc.)
  })
  .catch(error => {
    console.error('Error accessing media devices:', error);
  });
