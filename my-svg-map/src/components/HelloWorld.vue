<template>
  <div class="hello">
    <main>
      <section id="about">
        <h2>About Us</h2>
        <p>Insert information about your research group and its mission here.</p>
      </section>
      <section id="research">
        <h2>Research</h2>
        <p>Insert information about your research projects and interests here.</p>
      </section>
      <section id="publications">
        <h2>Publications</h2>
        <p>Insert a list of your publications here, with links to full text if available.</p>
      </section>
      <section id="people">
        <h2>People</h2>
        <p>Insert a list of your research group members here, with links to their individual pages if available.</p>
      </section>
      <section id="contact">
        <h2>Contact</h2>
        <p>Insert contact information for your research group here, including email addresses and phone numbers.</p>
      </section>
    </main>

  </div>
</template>

<script>
export default {
  name: 'HelloWorld',
  props: {
    msg: String
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
  margin: 40px 0 0;
}

ul {
  list-style-type: none;
  padding: 0;
}

li {
  display: inline-block;
  margin: 0 10px;
}

a {
  color: #42b983;
}</style>
