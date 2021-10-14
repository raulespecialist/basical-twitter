const app = new Vue({
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
              console.log('response.data');
              console.log(response.data);
              console.log('response.data');
              this.tweets = response.data;
              console.log(this.tweets[0].name);
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
		console.log(response);
	  })
	  .catch(function (error) {
		console.log(error);
	  })
	  .then(function () {
	  });
    }

  }
})