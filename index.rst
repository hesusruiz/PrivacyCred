

PrivacyCred and the eHealth Network Trust Framework
===================================================

In the blockchain space, many people and many projects put the technology first and then the citizen, trying to hack privacy and data protection into a system that was not designed with those requirements from the beginning.

Surprisingly, this also applies to many implementations and initiatives in the Self-Sovereign Identity (SSI) space, where many initiatives insist on registering and recording the identities of citizens in a globally shared infrastructure, even though it is not really required or desirable for many important use cases.

Even though they claim that they use cryptographic techniques (from hashes to Zero-Knowledge Proofs) to achieve privacy, many claim so without a proper PIA (Privacy Impact Assessment) of the actual implementation in a concrete system. And most importantly, they assume that registering the identities of citizens is required, without a proper justification, violating the principle of minimisation and proportionality.

To make things worst, due to the COVID-19 pandemia there has been a proliferation of initiatives and projects advocating the use of Verifiable Credentials and blockchain technologies, but lacking the principle of "citizen first, technology last". Those initiatives tend to be the most publicised, creating a generalised distrust on blockchain for use cases where strong privacy and citizen protection is critical.

.. rubric:: Interoperability of health certificates Trust framework

However, the recent Guidelines from the eHealth Network, especially the document on interoperability of the Trust Framework (`Interoperability of health certificates Trust framework`_) have made clear the requirements and characteristics that such solutions must comply with, striking the right balance between citizen and public health.

.. _`Interoperability of health certificates Trust framework`: https://ec.europa.eu/health/sites/health/files/ehealth/docs/trust-framework_interoperability_certificates_en.pdf

Even though the documents assume centralised technology for implementation,

- they provide leeway in some areas where proper use of blockchain technology and Verifiable Credentials could add value, complementing and enhancing the solution delineated in the Guidelines while maintaining the principles of **strong privacy and data protection**, **cross-border interoperability**, **inclusiveness** and **simplicity and user-friendliness**.
- the Guidelines can be generalised to be used for the correct implementation of many different use cases in many industries (not limited to Covid-19 certificates), ensuring that the same principles mentioned above are implemented.

.. rubric:: Applying the Guidelines to the Blockchain

The rest of the document uses the Guidelines from the eHealth Network to show how correct applications using W3C Verifiable Credentials and blockchain should be implemented.

Especifically, we describe the :doc:`PrivacyCred <ssi/privacycred>` system, which is is
designed specifically for some important use cases where especially sensitive personal
data is handled. A high degree of privacy and unlinkability is the first design criteria.
It also supports scenarios where physical, on-person verification of identity of holder is
needed and where normal W3C Verifiable Credential flows are not fully suitable as they are
normally designed currently.


.. toctree::
   :numbered:
   :hidden:
   :maxdepth: 3
   :caption: Contents

   ssi/introduction
   ssi/annotehealth
   ssi/privacycred
   ssi/references
   
   