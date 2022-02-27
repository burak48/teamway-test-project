import { shallowMount } from '@vue/test-utils';
// import flushPromises from 'flush-promises';
import Question from '../../src/components/Question.vue';

const mockQuestions = [
  {
    question: 'QUESTION 1',
    options: {
      a: 'OPTION A',
      b: 'OPTION',
      c: 'OPTION',
      d: 'OPTION',
    },
    answer: 'c',
  },
  {
    question: 'QUESTION 2',
    options: {
      a: 'OPTION A',
      b: 'OPTION B',
      c: 'OPTION C',
      d: 'OPTION D',
    },
    answer: 'd',
  },
];

jest.mock('axios', () => ({
  get: () =>
    Promise.resolve({
      data: mockQuestions,
    }),
}));

describe('Question.vue', () => {
  //   describe('when API call is successful', () => {
  //     it('should return question list', async () => {
  //       const wrapper = shallowMount(Question);
  //       await flushPromises();
  //       expect(wrapper.vm.questions.length).toBe(2);
  //     });
  //   });

  describe('when API call fails', () => {
    it('should return empty question list', () => {
      const wrapper = shallowMount(Question);
      expect(wrapper.vm.questions).toEqual([]);
    });
  });
});
