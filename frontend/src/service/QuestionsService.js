import axios from 'axios';
import BASE_API_URL from './urls';

const QUESTIONS_DATA = '/questions/';

class QuestionsService {
  getQuestionData(parameters) {
    return axios.get(`${BASE_API_URL}${QUESTIONS_DATA}?${parameters}`);
  }
}
export default new QuestionsService();
