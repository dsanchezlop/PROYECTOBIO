<template>
  <div class="hello">
    <main>
      <section id="about">
        <h2>About Us</h2>
        <p>We are a group of students from Catalonia that wanted to present information about how the fertilizers are affecting our ecosystem.</p>
      </section>
      <section id="research">
        <h2>Research</h2>
        <p>We grouped the data from several sources to present it in a comfortable and easy-to-read way</p>
      </section>
      <section id="publications">
        <h2>Publications</h2>
        <p>We acquired the data for this project from these sources:</p>
        <a href="https://www.nature.com/articles/s41597-022-01395-2">Nature: A global dataset to parametrize critical nitrogen dilution curves for major crop species</a>
        <a href="https://ourworldindata.org/fertilizers#explore-data-on-fertilizers">Our world in data: A global dataset of fertilizer data</a>
      </section>
      <section id="contact">
        <h2>Contact</h2>
        <p>We have a contact form where you can message us about any questions you may have</p>
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

<style></style>
