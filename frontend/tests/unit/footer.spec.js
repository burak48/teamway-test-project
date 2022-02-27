import { shallowMount } from '@vue/test-utils';
import Footer from '../../src/components/Footer.vue';

describe('Footer.vue', () => {
  describe('footer component renders', () => {
    it('should render footer', () => {
      const wrapper = shallowMount(Footer);
      expect(wrapper.exists()).toBe(true);
    });
  });
  describe('footer component text', () => {
    it('should write Burak Saglam', () => {
      const wrapper = shallowMount(Footer);
      expect(wrapper.find('p').text()).toBe('Copyright © 2022 Burak Saglam');
    });
  });
});
