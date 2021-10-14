const app = new Vue({
    delimiters: ['${', '}'],
  el: '#app',
  data: {
    name: '',
    tweet: '',
    tweets:[]
  },
  methods: {
    loadTweets: function ()
    {
      axios.get('http://127.0.0.1:8000/api/twitter/').then(
          response => {
              console.log(response.data);
              this.tweets = response.data;
          })
          .catch(function (error) {
              console.log(error);
          })
          .then(function () {
          });
  },
    processForm: function ()
    {
	axios.post('http://127.0.0.1:8000/api/twitter/', {
		name: this.name,
        tweet: this.tweet
	  })
	  .then(function (response) {
		console.log(response.data);
          app.loadTweets();
	  })
	  .catch(function (error) {
		console.log(error);
	  })
	  .then(function () {
	  });
    }

  },
    created() {
        this.loadTweets();
    },
})