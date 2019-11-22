import Vue from "vue";
import Vuex from "vuex";

import { authModule } from './auth';
import { categoriesModule } from './categories';
import { productsModule } from './products';

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    loading: false,
  },
  getters: {
    isLoading: state => !!state.loading,
  },
  mutations: {
    loading(state, value) {
      state.loading = value;
    }
  },
  modules: {
    authModule,
    categoriesModule,
    productsModule
  }
});
