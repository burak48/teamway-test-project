<template>
  <div>
    <div id="container">
      <h1 id="headline">Questions</h1>
      <hr class="divider" />

      <div v-if="loading">Loading...</div>

      <div v-else>
        <div v-if="questionIndex < 5">
          <p>{{ questions[questionIndex].question }}</p>

          <label
            v-for="(option, index) in questions[questionIndex].options"
            :key="index"
            :for="index"
            :class="index == questions[questionIndex]['answer'] ? 'label-correct' : 'label-wrong'"
          >
            <input
              :id="index"
              v-model="selectedAnswer"
              type="radio"
              class="hidden"
              :value="index"
              :disabled="selectedAnswer != ''"
              @click="isAnswer(index)"
            />
            {{ option }}
          </label>
          <div class="btn-next-wrapper">
            <button v-show="selectedAnswer != ''" class="btn-next" @click="nextQuestion">
              Next Question &gt;
            </button>
          </div>
        </div>

        <div v-else>
          <h2 class="result-text">Your Score Result</h2>
          <div class="result">
            <p>
              Correct Answers:
              <span class="correct-text">{{ correctAnswer }}</span>
            </p>
            <p>
              Incorrect Answers:
              <span class="wrong-text">{{ wrongAnswer }}</span>
            </p>
          </div>
          <div class="btn-next-wrapper">
            <button class="btn-next" @click="reset">Start Over</button>
          </div>
        </div>
      </div>

      <hr class="divider" />
    </div>
  </div>
</template>

<script>
import QestionsService from '../service/QuestionsService';

export default {
  name: 'QuestionComponent',
  data() {
    return {
      questions: [],
      statusCode: 0,
      loading: true,
      questionIndex: 0,
      selectedAnswer: '',
      correctAnswer: 0,
      wrongAnswer: 0,
      count: 3,
    };
  },
  mounted() {
    this.fetchData();
  },
  methods: {
    fetchData() {
      const parameter = 'question_id=1'; // TEST
      QestionsService.getQuestionData(parameter)
        .then((response) => {
          this.questions = [];
          this.statusCode = response.status;
          if (response.status === 200) {
            if (Object.prototype.hasOwnProperty.call(response.data, 'result')) {
              this.questions = response.data.result;
              console.log('QUESTIONS', this.questions);
            }
          }
        })
        .catch((error) => {
          this.questions = [];
          if (error.response) {
            this.questions = 'error';
            this.statusCode = error.response.status;
          }
        })
        .finally(() => {
          this.loading = false;
        });
    },
    isAnswer(answer) {
      this.selectedAnswer = answer;
      if (this.selectedAnswer === this.questions[this.questionIndex].answer) {
        this.correctAnswer += 1;
      } else {
        this.wrongAnswer += 1;
      }
    },
    nextQuestion() {
      this.questionIndex += 1;
      this.selectedAnswer = '';
    },
    showResult() {
      this.questionIndex += 1;
    },
    reset() {
      this.questionIndex = 0;
      this.selectedAnswer = '';
      this.correctAnswer = 0;
      this.wrongAnswer = 0;
    },
  },
};
</script>

<style scoped>
label {
  display: block;
  width: 100%;
  margin-top: 4px;
  font-size: 16px;
  padding-top: 2px;
  padding-bottom: 2px;
  border: 1px solid gray;
  border-radius: 30px;
  text-align: left;
}
label:hover {
  cursor: pointer;
  background-color: lightgray;
}
.label-correct {
  background-color: lightgreen;
  border: 1px solid lightgreen;
}
.label-wrong {
  background-color: lightcoral;
  border: 1px solid lightcoral;
}
.btn-next-wrapper {
  display: flow-root;
  margin-top: 0.5rem;
}
.btn-next {
  float: right;
  padding-top: 0.5rem;
  padding-bottom: 0.5rem;
  padding-left: 1.25rem;
  padding-right: 1.25rem;
  font-size: 0.875rem;
  line-height: 1.25rem;
  font-weight: 700;
  letter-spacing: 0.025em;
  border-radius: 30px;
}
.result-text {
  font-size: 1.875rem;
  line-height: 2.25rem;
  font-weight: 700;
}
.result {
  margin-top: 1.5rem;
  margin-left: 1rem;
  display: block;
  justify-content: center;
}
.correct-text {
  color: #047857;
  font-size: 1.5rem;
  line-height: 2rem;
  font-weight: 700;
}
.wrong-text {
  color: #b91c1c;
  font-size: 1.5rem;
  line-height: 2rem;
  font-weight: 700;
}
</style>
