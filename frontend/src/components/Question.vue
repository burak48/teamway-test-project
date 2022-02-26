<template>
  <div>
    <article>
      <h1>Questions</h1>
      <div class="content">
        <p>
          Lorem ipsum dolor sit amet, consectetur adipisicing elit. Assumenda, et! Veniam, cum.
          Necessitatibus consectetur, alias facere, cum omnis officia ad architecto dolore rerum
          voluptatum fuga. Provident, voluptate voluptas? Dolor, blanditiis.
        </p>
        <p>
          Lorem ipsum dolor sit amet, consectetur adipisicing elit. Assumenda, et! Veniam, cum.
          Necessitatibus consectetur, alias facere, cum omnis officia ad architecto dolore rerum
          voluptatum fuga. Provident, voluptate voluptas? Dolor, blanditiis.
        </p>
        <p>
          Lorem ipsum dolor sit amet, consectetur adipisicing elit. Assumenda, et! Veniam, cum.
          Necessitatibus consectetur, alias facere, cum omnis officia ad architecto dolore rerum
          voluptatum fuga. Provident, voluptate voluptas? Dolor, blanditiis.
        </p>
      </div>
    </article>
  </div>
</template>

<script>
import QestionsService from '../service/QuestionsService';

export default {
  name: 'QuestionComponent',
  data() {
    return {
      questionData: [],
      statusCode: 0,
      loading: false,
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
          this.questionData = [];
          this.statusCode = response.status;
          if (response.status === 200) {
            if (Object.prototype.hasOwnProperty.call(response.data, 'result')) {
              this.questionData = response.data.result;
            }
          }
        })
        .catch((error) => {
          this.questionData = [];
          if (error.response) {
            this.questionData = 'error';
            this.statusCode = error.response.status;
          }
        })
        .finally(() => {
          this.loading = false;
        });
    },
  },
};
</script>

<style scoped>
article {
  background: var(--gray-color);
  padding: 1em;
  border-radius: 0 0 5px 5px;
  box-shadow: 5px 5px 5px #ccc;
  position: relative;
  z-index: -1;
}

h1 {
  font-size: 115%;
  margin: 1em 2em;
  padding: 0;
  position: relative;
  color: #777;
}

.content {
  padding: 0 0 0 3em;
  font-size: 16px;
}
</style>
