class AudioProcessor extends AudioWorkletProcessor {
    constructor() {
      super();
    }
  
    process(inputs, outputs, parameters) {
      const input = inputs[0];
      if (input.length > 0) {
        const channelData = input[0];
        let sum = 0;
  
        for (let i = 0; i < channelData.length; i++) {
          sum += channelData[i] * channelData[i];
        }
  
        const volume = Math.sqrt(sum / channelData.length);
  
        if (volume > 0.01) {
          this.port.postMessage('startRecording');
        }
      }
  
      return true;
    }
  }
  
  registerProcessor('audio-processor', AudioProcessor);
  