---
title: Contact
date: 2022-10-24

type: landing

sections:
  - block: contact
    content:
      title: Contact
      text: |-
        Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer tempus augue non tempor egestas. Proin nisl nunc, dignissim in accumsan dapibus, auctor ullamcorper neque. Quisque at elit felis. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae; Aenean eget elementum odio. Cras interdum eget risus sit amet aliquet. In volutpat, nisl ut fringilla dignissim, arcu nisl suscipit ante, at accumsan sapien nisl eu eros.
      email: g.vallee-tourangeau@kingston.ac.uk
      address:
        street: Kingston Business School, Kingston Hill
        city: Kingston-upon-Thames
        region: 
        postcode: 'KT2 7LB'
        country: United Kingdom
        country_code: UK
      coordinates:
        latitude: '51.4290'
        longitude: '0.2649'
      directions: Enter Kingston Business School Building and take the stairs on the right to Office 3012 on Floor 3
      office_hours:
        - 'Wednesday 10:00 to 11:00 (online)'
        - 'Thursday 16:00 to 17:00'
        - 'Friday 13:00 to 14:00'
      appointment_url: 'https://outlook.office.com/bookwithme/user/e55f508cc2fa4dc9b7d04a27f5c2b391@kingston.ac.uk/meetingtype/T-Pb3U5gl0So-Uqhm5lhhA2?anonymous&ismsaljsauthenabled&ep=mLinkFromTile'
      #contact_links:
      #  - icon: comments
      #    icon_pack: fas
      #    name: Discuss on Forum
      #    link: 'https://discourse.gohugo.io'
    
      # Automatically link email and phone or display as text?
      autolink: true
    
      # Email form provider
      form:
        provider: netlify
        formspree:
          id:
        netlify:
          # Enable CAPTCHA challenge to reduce spam?
          captcha: false
    design:
      columns: '1'

  - block: markdown
    content:
      title:
      subtitle: ''
      text:
    design:
      columns: '1'
      background:
        image: 
          filename: contact.jpg
          filters:
            brightness: 1
          parallax: false
          position: center
          size: cover
          text_color_light: true
      spacing:
        padding: ['20px', '0', '20px', '0']
      css_class: fullscreen
---
