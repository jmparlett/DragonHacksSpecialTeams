

let app = new Vue ({
  delimiters: ["[[", "]]"],
  el: '#title',
  data: {
    myData: 'Dragon Lifts'
  }, 
  methods: {
    create: function(){alert("This button doesn't work you fool!");}
  }
})


