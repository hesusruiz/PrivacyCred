
PrivacyConsent
==============

Once the PrivacyCred system is operating and the relevant legal entities are registered in the Trust Framework, the management of PrivacyConsent credentials is relatively easy, as it can be implemented using otherwise standard credentials using the underlying PrivateCred system, and benefiting from its specific privacy characteristics.

Credential issuance by first entity
-----------------------------------

The flow of issuance of a PrivacyConsent credential is mostly the same as any other credential. However, it includes some special items. The overall flow is:

.. figure:: images/PrivacyConsent_OverallFlow_1.png
    :width: 70%
    :align: center

    Credential issuance by first entity


- The citizen logs into the system of the Issuer Entity. If the entity is a private company, we assume that the citizen is already an existing customer and that the proper KYC processes have benn performed when the customer was onboarded. This process can also be performed over the phone if the business has a proper mechanism of identifying the customer in order to perform legaly binding transactions. If the entity is a public administration, we assume that the entity performs the identification with the nationally acceptable mecanisms, including in-person and remote mechanisms.

  This standard login process has to be performed at least once to have the legal backing of credentials issued in the following steps. After the credential issuance, the Issuer entity could use (if desired) the credential to perform automatic and remote login of the citizen.

- The citizen explicitly accepts to provide consent for a given purpose. The operation should be performed in the same way as if the customer were executing other legaly binding operations in the Issuer Entity system. This is acting effectively as a signature of the fact that the citizen is providing consent for a given purpose, including the consent to generate a digital vertifiable credential to facilitate some process.

- The Issuer Entity records the consent for future reference or auditing, as it is done currently without verifiable credentials.

- The Issuer entity then requests from the Citizen a new credential that should include a Peer DID that the Citizen generates with her mobile app. The credential should also be signed with the private key associated to that Peer DID. There may be several mechanisms for requesting and sending credentials. The PrivacyConsent system is based on PrivacyCred so it uses the same set of mechanisms, including QRs.

- The Issuer entity receives the credential from the Citizen and performs some validations. 

- The Issuer Entity generates a Verifiable Credential that includes the explicit consent and purpose, and the citizen Peer DID. The credential is digitally signed by the Issuer Entity with the private key associated to the public key registered in the Trust Framework. Including the Peer DID of the citizen, the credential is binding that Peer DID with the real identity of the citizen (as verified using the KYC data). And this binding is digitally signed by the Issuer Entity in a tamper-resistant way.

- The citizen receives the credential via the QR mechanism (or any other that is supported by the system).

After the interaction, both parties (citizen and Issuer Entity) have a digital representation of the informed consent:

- The Issuer Entity has a consent with a proof of citizen acceptance based on the KYC process that was performed when onboarding the citizen.

- The citizen has a credential digitally signed by the Issuer Entity attesting that the citizen provided consent and that it was accepted by the Issuer Entity.


Credential reception by second entity
-------------------------------------

After the previous process, the first entity has already the consent from the citizen. The process to send the consent to the second participating entity is based on the verification flows. The process is the following:

.. figure:: images/PrivacyConsent_OverallFlow_2.png
    :width: 70%
    :align: center

    Credential reception by second entity


The citizen interacts with the Verifier Entity. This could be done via different channels, like login into the system of the Verifier Entity, or in-person in the premises of the entity. It can also be performed via other electronic channels like email or even messaging systems. Here we describe the process for in-person interaction as when the citizen goes to the social services for the first time and she does not have yet any legally accepted identification mechanism to interact with the public administration. After the first interaction, all other interactions could be performed remotely.

The citizen uses her mobile app to generate a W3C Presentation object, which is essentially a digitally signed object including one or more credentials. The Presentation object is digitally signed with the private key associated to the Peer DID that was used when the process of generating the credential was performed by the first entity.

In this way, the Presentation object includes the following:

- The purpose of the consent.

- The proof that the Issuer Entity is attesting that it received the explicit consent from the customer, after identifying her.

- The signature of the whole thing using a private key associated to the Peer DID that the citizen provided to the Issuer Entity.



