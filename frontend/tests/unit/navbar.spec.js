import { shallowMount } from '@vue/test-utils';
import Navbar from '../../src/components/Navbar.vue';

describe('Navbar.vue', () => {
  describe('navbar component renders', () => {
    it('should render navbar', () => {
      const wrapper = shallowMount(Navbar);
      expect(wrapper.exists()).toBe(true);
    });
  });
  describe('navbar component text', () => {
    it('should write company logo', () => {
      const wrapper = shallowMount(Navbar);
      expect(wrapper.find('a').text()).toBe('CompanyLogo');
    });
  });
});
