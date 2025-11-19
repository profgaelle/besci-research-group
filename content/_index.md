---
# Leave the homepage title empty to use the site title
title:
date: 2022-10-24
type: landing

sections:
  - block: hero
    content:
      title: |
        Behavioural Science & Creative Insights (BeSCI)
      image:
        filename: welcome.jpg
      text: |
        We study the psychology of behaviour change and creative action.

        We're interested in the barriers and drivers of behaviour across contexts, whether that's pursuing creative practice, making sustainability-led decisions, making professional judgements, or getting vaccinated.
        
        Building on our work in health decisions and vaccine hesitancy, our current main focus is the study of creative cognition and practice: understanding creativity not just as a cognitive process, but as behaviour that people must initiate, sustain, and navigate obstacles to maintain.
        
        We use experimental psychology alongside practice-based methods—including lived experience.
  - block: markdown
    content:
      title: |
        Our Research
      subtitle: ''
      text: |
        **Creative Cognition**
        Understanding how people generate ideas, solve problems, and collaborate with AI systems to create. We study creativity as a distributed process involving both mental operations and physical actions within one's immediate environment.

        **Decision-Making & Uncertainty**  
        Investigating how people make judgments under uncertainty, from peer review evaluations to vaccine decisions. We examine the role of information design, autonomy, and cognitive biases.

        **Behavioural Change**
        Exploring what motivates behaviour change in sustainability, healthcare and organizational contexts. Our work informs policy and practice across sectors.

        ### Current Projects
          - Arts-based interventions for workplace wellbeing and organisational performance
          - Embodied and distributed cognition in art-making and creative problem-solving
          - Community-centered nature-based solutions for climate adaptation
          - The psychology of environmental choices and pro-environmental behaviour
          - The psychology of academic peer-review decision-making
    design:
      columns: '1'
      background:
        image: 
          # filename: coders.jpg
          filters:
            brightness: 0
          parallax: true
          position: center
          size: cover
          text_color_light: true
      spacing:
        padding: ['20px', '0', '20px', '0']
      css_class: fullscreen
  
  # - block: collection
  #   active: false
  #   content:
  #     title: Latest News
  #     subtitle:
  #     text:
  #     count: 5
  #     filters:
  #       author: ''
  #       category: ''
  #       exclude_featured: false
  #       publication_type: ''
  #       tag: ''
  #     offset: 0
  #     order: desc
  #     page_type: post
  #   design:
  #     view: card
  #     columns: '1'
  
  # - block: markdown
  #   content:
  #     title:
  #     subtitle: ''
  #     text:
  #   design:
  #     columns: '1'
  #     background:
  #       image: 
  #         filename: coders.jpg
  #         filters:
  #           brightness: 1
  #         parallax: false
  #         position: center
  #         size: cover
  #         text_color_light: true
  #     spacing:
  #       padding: ['20px', '0', '20px', '0']
  #     css_class: fullscreen

  # - block: collection
  #   content:
  #     title: Latest Preprints
  #     text: ""
  #     count: 5
  #     filters:
  #       folders:
  #         - publication
  #       publication_type: 'article'
  #   design:
  #     view: citation
  #     columns: '1'

  # - block: markdown
  #   content:
  #     title:
  #     subtitle:
  #     text: |
  #       {{% cta cta_link="./people/" cta_text="Meet the team →" %}}
  #   design:
  #     columns: '1'
---
