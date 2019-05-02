import { Todo } from './App';

enum States { LISTENING, ADDING }

export default class SpeechProcessorService {
  addTodoHandler: (transcript: string) => Todo[];
  toggleTodoHandler: (todo: Todo) => Todo[];
  state: States;
  speaker: SpeechSynthesisUtterance;
  // var speech_answer =  '';

  constructor(public todos: Todo[]) {
    this.state = States.LISTENING;
    this.speaker = new SpeechSynthesisUtterance();
    this.speaker.lang = 'en-US';
  }

  process(transcript: string) {
    if (this.state === States.LISTENING) {
      this.processListening(transcript);
    } else if (this.state === States.ADDING) {
      this.processAdding(transcript);
    }
  }

  getAnswer(transcript: string) {
    var that = this;
    console.log('Calling endpoint');
    fetch('http://hinckley.cs.northwestern.edu/~rbi054/whisper/update_answer.php', {
      method: 'POST',
      headers: new Headers({
                'Content-Type': 'application/x-www-form-urlencoded', // <-- Specifying the Content-Type
        }),
      body: `param1=${transcript}` // <-- Post parameters
    })
        .then(function (response) {
                        return response.text();
                    }).then(function(data) {
                        console.log(data);
                        var speechAnswer=data;
                        console.log('answer is');
                        console.log(speechAnswer);
                        that.speaker.text = speechAnswer;
                        speechSynthesis.speak(that.speaker);
                    }).catch(function (error) {
                        console.log('Request failed', error);
                        var speechAnswer='';
                        console.log(speechAnswer);
                    });

  }
  processListening(transcript: string) {
    this.getAnswer(transcript);

    console.log(transcript);
    if (transcript.includes('where am I')) {
      // this.state = States.ADDING;
      this.speaker.text = 'You are at the Block Museum in Evanston Illinois';
      speechSynthesis.speak(this.speaker);
    } else if (transcript.includes('what exhibit is this')) {
      this.speaker.text = 'Welcome to this exhibit titled Caravans of Gold, Fragments in Time';
      speechSynthesis.speak(this.speaker);
    } else if (transcript.includes('what is your favorite exhibit')) {
      this.speaker.text = 'My favorite is the Atlas of Maritime Charts by Abraham Cresque.';
      speechSynthesis.speak(this.speaker);
    } else if (transcript.includes('what works are on display')) {
      this.speaker.text = 'Jen Bervin, Dario Robleto, Kader Attia, Marie Watt, Walter Kitundu';
      speechSynthesis.speak(this.speaker);
    } else if ((transcript.includes('complete') || transcript.includes('toggle')) && transcript.includes('task')) {
      this.processToggling(transcript);
    } else {
      this.state = States.LISTENING;
    }
  }

  processAdding(transcript: string) {
    this.todos = this.addTodoHandler(transcript);
    this.state = States.LISTENING;
  }

  processToggling(transcript: string) {
    const index = this.mapNumber(transcript);
    if (index === -1) {
      return;
    }
    const todo = this.todos[index];
    this.speaker.text = `Task number ${index + 1} was toggled`;
    speechSynthesis.speak(this.speaker);
    this.todos = this.toggleTodoHandler(todo);
  }

  private mapNumber(transcript: string) {
    const numbers = [['one', 'first', '1'], ['two', 'second', '2'], ['three', 'third', '3'],
      ['fourth', '4'], ['five', 'fifth', '5']];
    return numbers.findIndex(numberSynonyms => numberSynonyms.some(synonym => transcript.includes(synonym)));
  }
}
