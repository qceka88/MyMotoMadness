# MyMotoMadness
 

# This is my Personal Project.





Try it:

[www.mymotomadness.eu](https://qceka88.pythonanywhere.com/)



Basically is a site for selling offers with sections for articles. Written on Django. Using a PostgreSQL as DB.

Not registered users are restricted. They can only watch the offers and read the articles.
If not registered user try to reach part of the site via URL. Will be redirected to Home Page.
Also can se who is owner of the offer.

Registered user have access to create a selling offers. After offer is created, goes to the approval section 
where Admin or Moderator check the offer. Offer can be approved or deleted. 
If the offer is approved will be visible for everyone. Normal users are restricted to reach trough URL
other users EDIT and DELETE pages of other users or to make changes or delete other users offers. 

It has two groups of administration. One is Moderators. 
They have right to update and delete normal users selling offers. To create, update and delete Acritles.
Moderators are alo restricted to edit or delete other users.


Admin have full CRUD rights for everything.

[UPDATE]:

1. Added search options by multiple criteria for all sale offers and articles and messages.
2. Added PM option. Users can Send, Create, Read, Delete messages.
3. Messages are separated on two sections. Received and sent.
4. Received messages can be marked as read or not read.
5. Users receive notification for new message on Email and with  notification button.
6. Added Pagination for SaleOffers, Articles, Messages, ApprovalSection.
7. Added button for admin section only visible for admins.
8. Change admin URL for safety. 
9. Added buttons for send message directly to owner in sale offers, and user details page.
10. Messages can be deleted in different times from sender  and receiver.


Home Page!

![img.png](readme_images/img.png)

Common Sale Offer Section

![common_offers.PNG](readme_images%2Fcommon_offers.PNG)

Log in form.

![log_in_form.PNG](readme_images%2Flog_in_form.PNG)

News Section

![news_section.PNG](readme_images%2Fnews_section.PNG)


Registration form.

![reg_form.PNG](readme_images%2Freg_form.PNG)

It has a top bar only for registered user. When the user is Admin/Mod.
Addition button is appear to show that on site have offers for approval.
Message button is visible from every registered user.  Admin button is visible
only from admins.

![top_bar_for_registered_users.PNG](readme_images%2Ftop_bar_for_registered_users.PNG)

Approval section is visible only for administrators and moderators.

![approval_section.PNG](readme_images%2Fapproval_section.PNG)


Form for create new bike selling offer is accessible for registered users.
It is similar to creation form for equipment and parts.
User is restricted to upload minimum 2 and maximum 8 picture.
In edit form for sale ad user cannot save the offer  
if he try to upload more than 8 pictures, or to leave sale ad with less than 2 pictures.

![add_bike_form.PNG](readme_images%2Fadd_bike_form.PNG)

In edit form of offers is has admin/mod part that is not vissible for normal users.

![admin-mod.PNG](readme_images%2Fadmin-mod.PNG)

Sale offer view. Three types of offer have similar view.

![offer1.PNG](readme_images%2Foffer1.PNG)
![offer2.PNG](readme_images%2Foffer2.PNG)


Only admins can see the part bellow to create or remove moderators and other administrators.

![admin-mod-profile.PNG](readme_images%2Fadmin-mod-profile.PNG)

Buttons for create/edit/delete articles is visible for Admin/Mod users.

![acritcles-admin-mod.PNG](readme_images%2Facritcles-admin-mod.PNG)

Common Articles section

![common_article_view.PNG](readme_images%2Fcommon_article_view.PNG)

Common Advices section is similar to News Section.

![articles.PNG](readme_images%2Farticles.PNG)

Change Password view.

![change-password.PNG](readme_images%2Fchange-password.PNG)


Profile section.

![profile_details.PNG](readme_images%2Fprofile_details.PNG)

Not approved offers are visible only for owner, admins, moderators.

![profile_details2.PNG](readme_images%2Fprofile_details2.PNG)

Messages Received view

![message_view.PNG](readme_images%2Fmessage_view.PNG)

Messages Details view is mixed with list view

![details_message.PNG](readme_images%2Fdetails_message.PNG)

Messages sent  view. When Message box is empty

![sent_messages_view.PNG](readme_images%2Fsent_messages_view.PNG)

Email greetings for registration.
![email_greetings.PNG](readme_images%2Femail_greetings.PNG)

Email notification for new message and link to message
![email_notification_for_message.PNG](readme_images%2Femail_notification_for_message.PNG)
