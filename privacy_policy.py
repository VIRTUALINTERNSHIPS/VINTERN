import streamlit as st 
import streamlit.components.v1 as com
st.set_page_config(layout="wide",page_title='VINTERN', page_icon="👩‍🎓",initial_sidebar_state="expanded")
from streamlit_extras.colored_header import colored_header
from streamlit_extras.add_vertical_space import add_vertical_space

com.html("""

         
         """)
import streamlit as st
from htbuilder import HtmlElement, div, ul, li, br, hr, a, p, img, styles, classes, fonts
from htbuilder.units import percent, px
from htbuilder.funcs import rgba, rgb


def image(src_as_string, **style):
    return img(src=src_as_string, style=styles(**style))


def link(link, text, **style):
    return a(_href=link, _target="_blank", style=styles(**style))(text)


def layout(*args):

    style = """
    <style>
      # MainMenu {visibility: hidden;}
      footer {visibility: hidden;}
     .stApp { bottom: 105px; }
    </style>
    """

    style_div = styles(
        position="fixed",
        left=0,
        bottom=0,
        margin=px(0, 0, 0, 0),
        width=percent(100),
        color="black",
        text_align="center",
        height="auto",
        opacity=1
    )

    style_hr = styles(
        display="block",
        margin=px(8, 8, "auto", "auto"),
        border_style="inset",
        border_width=px(2)
    )

    body = p()
    foot = div(
        style=style_div
    )(
        hr(
            style=style_hr
        ),
        body
    )

    st.markdown(style, unsafe_allow_html=True)

    for arg in args:
        if isinstance(arg, str):
            body(arg)

        elif isinstance(arg, HtmlElement):
            body(arg)

    st.markdown(str(foot), unsafe_allow_html=True)


def footer():
    myargs = [
        
        "🔍",link("https://twitter.com/ChristianKlose3", "About us"),
        "            ||  ",
        "📞",link("https://twitter.com/ChristianKlose3", "Contact Us"),
        "             ||    ",
        "❓",link("https://twitter.com/ChristianKlose3", "FAQ"),
        "            ||     ",
        "☑",link("https://twitter.com/ChristianKlose3", "Terms-and-Conditions"),
        "            ||     ",
        "🔐",link("https://twitter.com/ChristianKlose3", "Privacy Policy"),
        "            ||     ",
        "💳",link("https://twitter.com/ChristianKlose3", "Refund"),
        br(),
        "© 2023 Copyright: 🎓VINTERN"

    ]
    layout(*myargs)


if __name__ == "__main__":
    footer()

with st.sidebar:
    st.button("hi")


colored_header(
    label="Privacy Policy",
    description=" ",
    color_name="violet-70",
)    


st.markdown("""
This Privacy Policy relates to the collection, use and disclosure of personal data, including special or sensitive personal data, by VINTERN Intelligence Private Limited ("VINTERN", "we", or "our"). Personal Data is information relating to an individual ("you" or "your") as more fully defined herein below. VINTERN is committed to protecting your privacy and ensuring that you have a secured experience on our website and while using our products and services (collectively, "Products").

This policy covers the VINTERN website and all the subdomains under VINTERN.ai. Please refer to the following link to read our terms of service Terms and Conditions

This policy outlines VINTERN's, its subsidiaries and affiliated companies handling practices and how we collect and use the information you provide in the course of your use or access of our systems through online interfaces (e.g. website, mobile applications etc.) (collectively "Company Systems"). In this Privacy Policy, "Personal Data" means any information that can be used to individually identify a person and may include, but is not limited to, name, email address, postal or other physical addresses, title, and other personally identifiable information. By using our services or products, it will be deemed that you have read, understood and agreed to be bound by this policy detailed hereunder

We will be the processor of the Personal Data that is provided, collected and/or processed pursuant to this policy, except where otherwise expressly stated.

Applicability of the Policy
This policy shall apply to all information we collect through the Company Systems and/or in the course of your use of the services of VINTERN.
This policy does not apply to, nor does VINTERN take any responsibility for, any information that is collected by any third party either using Company Systems or through any links on the Company Systems or through any of the advertisements or through BOTS.
Information We Collect
We will only collect information which you share with us. You can choose what information you want to share with us. We will collect your information only if you choose to share it through the Company Systems. We will collect the following information about you or related to your use of the Company's Systems:

Any personal or PII that you may submit or may be required to submit for registration and continued use of the Company Systems or receive the services by VINTERN;
Your name, title, gender, date of birth, email address, telephone number (Home/work/mobile telephonic number), profile/display picture, login name, screen name, nickname, or handle, country/state/postcode or city of residence, postal or other physical address, name(s) of the school/university (including grades and graduation year),name(s) of the workplace, job position/designation (including salary), resume/CV, information related to social profiles, such as Facebook, Google, GitHub etc., IP addresses and other information collected passively (as further detailed in the "Passive Collection" section below), may be collected; and
Any other information you may choose to further provide us, without limitation, any information to update your account and profile, if required, to fill out any forms, provide your feedback to surveys, write any articles on the Company Systems, or to use any features of Company Systems.
We collect and/or process your Personal Data as a part of the following activities related to our Products:

Account registration, use of certain Product features, creating or taking tests, generating reports based on information collected from use of our Products.
Requesting service and support for our Products and providing such support, registering for an event, participating in an online survey, participating in discussion groups or forums.
Registering for newsletter subscriptions, customizing the content you see as per relevance.
Please do not include any personal information, personally identifiable information or sensitive personal information unless specifically requested by VINTERN as part of the registration or other applicable processes. If VINTERN determines that any information you have provided or uploaded violates the terms of this policy, VINTERN shall have the right, in its absolute discretion, to delete such information without incurring any liability.

We may also periodically use your information received from your affiliated entities, business partners and other third-party sources and combine it with your account information. For example: if you access or login to our Company Systems via a third-party source like Facebook, Twitter, LinkedIn, we may receive your registration information, updated information and combine that with information we collect through our Company Systems or add it to your account information on our Company Systems.

If You are governed by the United States laws, to the extent permitted by applicable laws, we may obtain reports from public records of credit history checks, criminal databases checks including National Criminal Database and county courts in each state, national government restricted lists, sex offender registrations. If you are outside of the United States, to the extent permitted by applicable laws, VINTERN may obtain reports of the respective criminal background or registered sex offender checks. To obtain such reports as stated herein, we may use your information, like your full name and date of birth.

General Data Protection Regulation (GDPR) is designed to give EU citizens more control over their data. It aims to use an all-encompassing privacy and security law to safeguard Personal Data. Irrespective of their location, GDPR applies to all the relevant controllers or processors who deal with the Personal Data of EU citizens.

For more information, please refer to GDPR

Processing your Personal Data
We will use your Personal Data only in accordance with this policy. To enable us to fulfil the contract between us for the services you have requested, we need to process your Personal Data for purposes including the following:

Account registration.
Use of our website.
Creating or taking online tests.
Generating reports based on information collected from use of our Products.
Requesting service and support for our Products and providing such support.
Registering for hackathons.
Participating in discussion groups or forums.
Customizing the content you see as per relevance.
Referring your profile to relevant job opportunities.
We process Personal Data for purposes such as:
Providing reports based on information collected from use of our Products.
Keeping you up-to-date about latest Product announcements, software updates, software upgrades, system enhancements, special offers, and other information.
Providing support and assistance for our Products.
Providing the ability to create personal profile.
Providing the ability to contact you, if required.
Providing customer feedback and support.
Providing and administering opt-in events or other marketing or promotional activities on VINTERN.
Being able to conduct questionnaires and surveys in order to provide you with better products and services.
Supporting recruitment inquiries.
Personalizing marketing communication and website content based on your preferences, such as in response to your request for specific information on products and services that may be of interest to you.
Meeting contract or legal obligations.
We may allow employers to view your anonymised profile and contact you for a relevant job opportunity. We provide them with a channel to contact you for a relevant job opportunity. We share your PII with employers only with your explicit consent, or when you reply back to the conversation channel. If you wish to opt-out of this feature, please send us an email to contact@VINTERN.ai

We may also process your personal data where it is in our legitimate interests to seek professional advice, including, in connection with any legal proceedings (including any prospective legal proceedings), for obtaining legal advice or for establishing, exercising or defending legal rights.

Consent
How do we use your information?
VINTERN will use your Personal Data only in accordance with this policy. If you do not wish us to continue using your Personal Data in this manner you can request for deactivation of your account from account settings.

We will only process your Personal Data if we have a lawful basis for doing so, which includes but is not limited to the following:

consent, contractual necessity (i.e. processing that is necessary for the performance of a contract with you, such as your user agreement with us that allows us to provide you with the Products) and our legitimate interests or the legitimate interest of others (e.g. our users) such as:

Provide you with the websites and services, together with any support you may request.
Respond to your inquiries or fulfill your requests.
Diagnose Website and Service technical problems.
Send you information that we believe may be of interest to you, such as Service.
Announcements, newsletters, educational materials, and event information.
Send you administrative information such as notices related to the Services or policy changes.
Understand how the Websites and Services are being used in order to enhance and optimize them.
Prevent, detect, mitigate, and investigate fraudulent or illegal activity.
As described to you at the point of collection of the information.
Complying with our legal obligations, resolving disputes with users, enforcing our agreements.
Protecting, investigating and deterring against fraudulent, harmful, unauthorized or illegal activity.
How do we organize & store your data?
AWS Relational Database - Main database storing all User information.
ElasticSearch - Indexed resumes. We use it to query on text written in a user's resume.
Sentry - Used to monitor errors.
New Relic - Stores server logs which are used in optimization of our services.
S3 - Server logs and User resume files.
Google Analytics - The third-party services described in this section enable VINTERN to monitor and analyze Website and Service traffic. Google Analytics (Google Inc.) Google Analytics is a web analysis service provided by Google Inc. Google utilizes the information collected to track and examine the use of the Websites and Services to prepare reports that may be used for optimization of the Websites and Services. Information collected: Cookies and usage data.
Place of processing: United States.
Your Rights:
Rights: You have certain rights with respect to your Personal Data as mentioned below.

Access: You can request more information about the Personal Data we hold about you. You can also request a copy of the Personal Data.
Correction: If you believe that any Personal Data we are holding about you is incorrect or incomplete, you can request that we correct or supplement such data. You can also correct some of this information directly through your user profile or profile/account settings after logging into VINTERN. Please contact us as soon as possible upon noticing any inaccuracies or incompleteness.
Objection: You can contact us to let us know that you object to the collection or use of your Personal Data for certain purposes.
Erasure: You can request that we delete some or all of your Personal Data from our systems. While this will be done immediately, residual data may be saved in certain logs and this will be purged within a year after deleting your data. Once your data is deleted, you will no longer have an account with VINTERN.
Restrictions: You can always request us to deactivate your VINTERN account to restrict further processing of your Personal Data
Portability: You have the right to ask for a copy of your Personal Data in a machine- readable format.
Withdrawal of consent: If we are processing your Personal Data based on your consent (as indicated at the time of collection of such data), you have the right to withdraw your consent at any time. Please note, however, that if you exercise this right, you may have to then provide express consent on a case-by-case basis for the use or disclosure of certain of your Personal Data, if such use or disclosure is necessary to enable you to utilize some or all of our Products.
Retention
Your data is retained with VINTERN as long as you have an active account on the Company Systems. You can delete all of your Personal Data from our systems from your account profile page. Residual data may be saved in certain logs and this will be purged within a year after deleting your data. Once your data is deleted, you will no longer have an account with VINTERN.

Passive Data collection:
VINTERN might automatically collect some data about you when you are using any of our products, using methods like cookies and other tracking technologies. Information automatically collected includes cookies, page views, geolocation data, IP(internet protocol) addresses, browser and OS(Operating System) type, ISP (Internet Service Provider), files viewed and downloaded from our websites, referral and exit pages and click stream data. Such data does not have an expiry date and we do not delete this data. This data is stored in the form of logs or in third party tracking and analytics softwares like Google analytics, Linkedin Insights etc.

We Use Cookies:
VINTERN uses cookies to help us remember and process the items in your shopping cart. They are also used to help us understand your preferences based on previous or current site activity, which enables us to provide you with improved services. We also use cookies to help us compile aggregate data about site traffic and site interaction so that we can offer better site experiences and tools in the future. Further, we may use cookies or other tracking technologies to analyze trends, track users' movements around the website, and gather information about our user base, such as location information based on IP addresses.
You can choose to have your computer warn you each time a cookie is being sent, or you can choose to turn off all cookies. You do this through your browser (like Internet Explorer) settings. Each browser is a little different, so look at your browser's Help menu to learn the correct way to modify your cookies.
If you disable cookies off, some features will be disabled. It won't affect the user's experience that makes your site experience more efficient and some of our services will not function properly.
VINTERN may collect information related to visitors and machines. Such information includes cookies, IP addresses, pageview activities, and geolocation data. The details of user activities on our website such as number of visits, time spent on our website, and pages clicked are also collected.
To whom we may disclose your Personal Data:
General: The information you provide on the Company Systems may be disclosed by VINTERN to its employees, agents, representatives, consultants, subsidiaries, affiliates and third-party providers who require the information for the purposes of (a) operating and maintaining the Company Systems, (b) data processing or storage.

Hiring Partners: We may provide your data to our hiring partners after taking your consent. We provide resumes, phone numbers, email addresses and other relevant information to our hiring partners to enable users to get job offers. Events of Reorganization: In any given instance, if VINTERN undergoes any events of reorganization, merger, acquisition, insolvency or bankruptcy, VINTERN may sell, transfer or share some or all of our assets, including your information, subject to notification to You pertaining to transfer of Your information.

Applicable Laws: VINTERN will comply with requests and directions of all governmental, law enforcement, court or regulatory authorities, which it believes in good faith to be in accordance with any applicable law. Such compliance may include disclosing to the governmental, law enforcement, courts, or regulatory authorities' information submitted by you or collected in relation to your use of the Company Systems or VINTERN's services including any personally identifiable information. By using the Company Systems and receiving VINTERN services, you consent to VINTERN's disclosure of information as set out in this Section herein to governmental, law enforcement, courts or regulatory authorities

VINTERN will not publish, sell or rent Your personal information to third-parties for their marketing purposes without Your explicit consent.

Data Security:
The information that you provide, subject to disclosure in accordance with this policy, shall be maintained in a safe and secure manner. Your information shall be protected, to a commercially reasonable extent, against unauthorized access, use, or disclosure. Our databases and information are stored on secure servers with appropriate firewalls. Further, we use vulnerability scanning and scanning to PCI standards annually and our Company Systems are subject to regular Malware Scanning. Additionally, we use SSL certificate to encrypt all the data being transferred.

As a user of the Company Systems, you have the responsibility to ensure data security. You must not disclose to any person the authentication parameters that are assigned to you including Your username or password for your use of the Company Systems. You acknowledge that you will be solely responsible for all acts committed by use of your username /other authentication parameters.

Given the nature of internet transactions, VINTERN does not take any responsibility for the transmission of information collected from you or are generated by your use of the Company Systems or the services. Any transmission of such information over the internet is done at your sole risk. VINTERN does not take any responsibility for you or any third party circumventing the privacy settings or security measures contained on the Company Systems.

Notwithstanding anything to the contrary, while VINTERN will use all reasonable efforts to ensure that any information collected from you or are generated by your use of the Company Systems or the services is safe and secure, it offers no representations or warranties that the security measures are adequate, safe, fool proof or impenetrable.

Integration with Linked Websites and Third-Party Websites:
Links to external, or third-party websites, may be provided solely for your convenience. Such links from us to an external website does not imply or mean that VINTERN endorses or accepts any responsibility for the content or the use of such a website. VINTERN does not give any representation regarding the quality, safety, suitability, or reliability of any external websites or any of the content or materials contained in them. It is important for you to take necessary precautions, especially to ensure appropriate safety from viruses, worms, Trojan horses and other potentially destructive items.

Third-party Ad Networks:
Our Website may use third party network advertisers to display advertisements about our Products on third party websites, based on your visits to our site as well as other websites. This enables us and these third parties to target advertisements by displaying ads for our Products which might interest you.

Third party network advertisers' services may use cookies, JavaScript, and other technologies to make their ads effective and to personalize them to connect to you. These third-party cookies and other technologies are governed by each third party's specific privacy policy, and not this one. We may provide these third-party advertisers with anonymized and aggregated information about your usage of our website and our Products; however, we do not share your Personal Data with these third parties. You also have the option of denying the access of data to such third-party ad networks.

Anonymized Information:
Notwithstanding anything to the contrary in this policy, VINTERN may use any information provided to VINTERN in relation to or as part of the services in providing services to its other clients and to develop and create reports, statistical analysis, and benchmarking analyses for its clients provided that such reports contain only anonymous, aggregated data and do not identify you by name.

Age Restrictions:
You explicitly agree you are 18 years of age or older, unless represented by a parent or legal guardian. If you are not of the requisite age you must not provide any information to VINTERN directly or by way of usage of the Company Systems. If VINTERN determines that it is in possession of any information belonging to an individual below 18 years of age which is submitted, collected or generated in breach of the terms of this Policy, it will delete the same without any notice to the individual to whom such information belongs to.

Update
This policy may be updated from time-to-time so we recommend that you regularly review this policy each time you return to our website.



Contact:
This policy must be read in conjunction with the other agreements you may enter into with VINTERN and the ToS as published by VINTERN on VINTERN's website. By accepting the policy, you expressly consent to VINTERN's use and disclosure of your personal information in accordance with this policy.""")
