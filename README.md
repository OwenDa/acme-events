# Acme Events 
*Acme Events* is a portfolio site with a sense of humour. Ostensibly, the company organises and sells tickets to events at which would-be consumers can view the latest and greatest in the way of anvils.

An anvil is a blacksmithing tool more familiar to many as the heavy object often dropped on cartoon characters and made famous in this regard by Warner Brothers' Looney Tunes animations. Like almost all products within these Warner Bros. productions, anvils often bore a manufacturer's mark crediting them to ["Acme Corp."](https://en.wikipedia.org/wiki/Acme_Corporation). The ficticious corporation has since become a standin or placeholder wherever a fake company is needed and is even used in some jurisdictions Law Schools Admissions Tests as the plaintiff or defendent in example cases.

For the purely fictional business represented by this portfolio project, therefore, the company in question is "Acme Events". As the products showcased at the events do not matter and the purpose of the site is to demonstrate an online booking system for an events company, anvils were chosen as a humorous stand-in.
  
## Contents
1. [Problem Statement](#problem-statement)  
2. [User Stories](#user-stories)
3. [Tech Stack](#tech-stack)  
4. [Design Statement](#design-statement)
5. [Features](#features)
    + [Future Features](#future-features)
6. [Testing](#testing)
7. [Deployment](#deployment)  
8. [Known Bugs](#known-bugs)
9. [Credits](#credits)  
  
## Problem Statement  
Events companies advertising online face a unique version of a common problem; they wish to capture the consumer's full attention at the point of peak interest and prompt the user to take action, however, the event itself may be at a distant point in the future. The ability to sell tickets or take bookings in advance therefore represents a tremendous advantage to their business.

Third-party platforms to meet this need are in no shortage; however, a percentage of ticket sales is usually lost to platform fees, and the business loses control over how their material is represented when it's rendered on another site. In addition, consumer interest may be lost as the customer clicks through to the platform and is often taken away from the event company's own website. In addition, such platforms depend on their revenue from maximising tickets sales across all events, and may therefore advertise related and even competing events to the customer. In short, the interests of the company and the platform are not entirely aligned.

Ideally therefore, an event company would have its own native booking system with integrated payment through a secure, reputable payment processing service. Such a system would not take the consumer-user away from the site and would allow them to make multiple bookings, even across multiple events, without leaving the site.

While many future features may yet be implemented, Acme Events demonstrates this solution in practice.
  
## User Stories  
  **Types of User** 
  + Site Owner/Admin
  + Consumer-user
  + Browsing-user
   
  **As a site owner/admin, I can...** 
  + Advertise upcoming events with all relevant details concerning time, date, location and description.  
  + Link to this event-specific information from my social media (e.g. Facebook Event pages etc.)
  + Edit event details where necessary.  
  + Delete events if cancelled before their start date.  
  + Rely on automated processes within the site to display only those events that have not already passed (ie. expired events will not be presented to the public).  
  + Take bookings (sell tickets) online with ease and minimum investment of time.  
  + Link to and promote venues hosting these events to promote good relations between organiser and venue.  
  + Provide contact information for venues to reduce queries from users that would be more appropriately directed to the venue than the event organiser.  
  + Build a client contact database directly from my website using the integrated newsletter sign-up form.  
  + Access a receipt for each customer transaction through the Stripe dashboard.  
  
**As a browsing-user, I can...** 
  + View key information concerning upcoming events at a glance (e.g. location, time, date, etc.) 
  + Easily browse this list of events in chronological order, without the confusion or distraction that might be caused by also seeing expired events.  
  + View more detailed information about a specific event that interests me.  
  + Share a specific event on social media or elsewhere with its dedicated link, for example, if I wish to invite a friend (event-detail view).  
  + Sign up to a newsletter if I wish to remain informed about upcoming events or the company in general.  
  + Create an account to save time at checkout if ever I become a consumer-user.  
  + View the website's privacy policy in a new tab.  
  + Access information about event venues, such as contact details and address.  
  + Access a venue's website or its location within an online map service with a single click. 
  
**As a consumer-user, I can...** 
  + Make one or more bookings for one or more events I may wish to attend.
  + Pay online through a secure, reputable payment processing service integrated directly into the event website.
  + Receive feedback from the site assuring me that a given event booking has been created in my "cart".  
  + Update my cart by increasing or decreasing the quantity of tickets I wish to book for any given event.  
  + Update my cart by deleting an event booking entirely. 
  + Receive realtime feedback from the site when I update my cart.   
  + Save time at checkout by reusing default information saved to my account.  
  + View my past purchases in a dedicated "My Bookings" profile section.  
  + Update my default information at checkout or within the "My Bookings" profile section of the site.  
  + Receive realtime feedback about any errors in my input, such as form errors or erroneous card details.  

These functions should also be available to users employing a screen reader. See [Accessibility Testing](#accessibility-testing).


# Credits:
- Hero Image (anvil) <a href="https://www.freepik.com/free-photo/close-up-photo-shoot-hammer-anvil-dark-smith-workshop_24917063.htm#query=anvil&position=1&from_view=search&track=sph">by fxquadro on Freepik</a>.  
- Helpful article on Django slugs <a href="https://learndjango.com/tutorials/django-slug-tutorial">from Learn Django</a>.  
<!-- - <a target="_blank" href="https://icons8.com/icon/77797/metal">Site Favicon: "Metal"</a> icon by <a target="_blank" href="https://icons8.com">Icons8</a> -->