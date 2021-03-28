
Welcome to PrivacyCred's documentation!
=======================================

PrivacyConsent is a system that allows a citizen to manage informed consent to two independent
entities to exchange personal data among them for a very specific purpose. PrivacyConsent is based
on PrivacyCred, a generic credential system which is designed to be secure, privacy-preserving,
scalable, performant and robust.

PrivacyCred is designed specifically for some important use cases where especially sensitive
personal data is handled, like when people at risk of exclusion is involved or with some health data
flows. A high degree of privacy and unlinkability is the first design criteria. It also supports
scenarios where physical, on-person verification of identity of holder is needed and where normal
W3C Verifiable Credential flows are not fully suitable as they are normally designed currently.

**PrivacyCred**

The first part describes the :doc:`PrivacyCred <privacycred>` system, including the data model, interfaces and main
interactions. Understanding the caharacteristics of the underlying system is important to understand how PrivacyConsent works.

**PrivacyConsent**

The second part describes the :doc:`PrivacyConsent <privacyconsent>` flows on top of PrivacyCred for a very strict use case:
managing the informed consent of a user in the collective of people at risk of exclusion, when two or more entities are involved in the secure and legal exchange of sensitive personal data, to collaborate to provide a better service to the citizen.



.. toctree::
   :numbered:
   :hidden:
   :maxdepth: 2
   :caption: Contents

   privacycred
   privacyconsent


