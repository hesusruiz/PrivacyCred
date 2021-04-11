
DID Methods
===========

For generating credentials PrivacyCred uses two DID Methods (Peer DID and ELSI), but can interoperate with credentials generated with other DID Methods like EBSI, AlastriaID and Ethr.

Personally Identifiable Information (PII) is essentially very different from the public information from businesses and organisations. Those differences are even stressed in different regulations. The GDPR applies strict rules for processing PII.

This is the reason why PrivacyCred uses two different DID Methods, one for identities of organisations and another one for citizens.

For citizens we use Peer DIDs, with no requirement to register anything related to the citizen in any global repository or blockchain. Peer DIDs are perfect for maximising privacy in bilateral relationships where the actual DID and related data is only known to the parties involved in a relationship (the citizen and the organisation). Beyond bilateral relationships, Peer DIDs can also be very good when those relationships involve a reduced number of participants that agree to collaborate on some specific use case for a very well defined purpose and for the benefit of the citizen.

For organisations PrivacyCred uses ELSI, a DID method based in current standards which is extremely easy to implement and use, and is alligned completely with uses cases in the real economy, where the identities of organisations is public.

PrivacyCred is designed for managing very sensitive personal data, and this is the reason why we use two different DID Methods, one for identities of organisations and another one for citizens. This separation has many advantages, allowing a strict separation of the mechanisms that are used for managing those two very different sets of data.

For Citizens: Peer DID Method
-----------------------------

Advantages of Peer DIDs:

- They have no transaction costs, making them essentially free to create, store, and maintain.
- They scale and perform entirely as a function of participants, not with any central system's capacity.
- Because they are not persisted in any central system, there is no trove to protect.
- Because only the parties to a given relationship know them, concerns about personal data and privacy regulations due to third-party data controllers or processors are much reduced.
- Because they are not beholden to any particular blockchain, they have minimal political or technical baggage.
- They can be mapped into the namespaces of other DID ecosystems, allowing a peer DID to have predictable meaning in 1 or more other blockchains (see Grafting). This creates an interoperability bridge and solves a problem with blockchain forks fighting over the ownership of a DID.
- Because they avoid a dependence on a central source of truth, peer DIDs free themselves of the often-online requirement that typifies most other DID methods, and are thus well suited to use cases that need a decentralized peer-oriented architecture. Peer DIDs can be created and maintained for an entire lifecycle without any reliance on the internet, with no degradation of trust. They thus align closely with the ethos and the architectural mindset of the local-first and offline-first software movements.


For Organisations: ELSI DID Method
----------------------------------

The system supports several DID Methods using the Universal Resolver to resolve each DID into a corresponding DID Document.
But the main DID Method used for legal persons, anchored into a Public-Permissioned blockchain, is *ELSI*: `did:elsi`.

ELSI DID syntax
***************

The name ELSI stands for **E**\TSI **L**\egal person **S**\emantics **I**\dentifier, because it is based on the *Legal person semantic identifier* defined in the `European Norm ETSI EN 319 412-1 <https://www.etsi.org/deliver/etsi_en/319400_319499/31941201/01.04.02_20/en_31941201v010402a.pdf>`_, related to digital signatures, peer entity authentication, data authentication as well as data confidentiality.

The ELSI DID Method refers only to legal persons, so we are using the *id-etsi-qcs-SemanticsId-Legal* definition described in Section 5.1 of ETSI EN 319 412-1.

Creating a DID is extremely simple and fully decentralized (does not require participation of any central authority), assuming that the legal person already exists. Its definition using ABNF syntax is:

::

    did = "did:elsi:" id-etsi-qcs-SemanticsId-Legal

Which is the concatenation of the prefix `did:elsi:` with the legal person identifier defined in ETSI EN 319 412-1. For the full syntax, please refer to the standards document, but for the two most common basic identifiers (VAT and LEI) the identifier is composed of: 

- 3 character legal person identity type reference, like `VAT` for identification based on a national value added tax identification number or `LEI` for the `Legal Entity Identifier <https://www.gleif.org>`_.
- 2 character ISO 3166 [2] country code;
- hyphen-minus "-" (0x2D (ASCII), U+002D (UTF-8)); and
- identifier (according to country and identity type reference).

Some examples of DIDs are the following:


+-------------------------------------------------+-----------------------------------------+
| Name                                            | DID                                     |
+=================================================+=========================================+
| ENDESA ENERGÍA (www.endesa.com)                 | **did:elsi:VATES-A81948077**            |
+-------------------------------------------------+-----------------------------------------+
| IN2 (www.ins.es)                                | **did:elsi:VATES-B60645900**            |
+-------------------------------------------------+-----------------------------------------+
| AENA (www.aena.es)                              | **did:elsi:VATES-A86212420**            |
+-------------------------------------------------+-----------------------------------------+
| Inter-American Development Bank (www.iadb.org)  | **did:elsi:LEIXG-VKU1UKDS9E7LYLMACP54** |  
+-------------------------------------------------+-----------------------------------------+
| DAA plc (Dublin Airport Authority) (www.daa.ie) | **did:elsi:LEIXG-635400HRFGVKXFHZ8O77** |
+-------------------------------------------------+-----------------------------------------+

ELSI DID Document
*****************

An example DID Document is the following:

.. code-block:: json

    {
    "payload": {
        "@context": [
        "https://www.w3.org/ns/did/v1",
        "https://w3id.org/security/v1"
        ],
        "id": "did:elsi:VATES-B60645900",
        "verificationMethod": [
        {
            "id": "did:elsi:VATES-B60645900#key-verification",
            "type": "JwsVerificationKey2020",
            "controller": "did:elsi:VATES-B60645900",
            "publicKeyJwk": {
            "kid": "key-verification",
            "kty": "EC",
            "crv": "secp256k1",
            "x": "3K4iNuzPkcrHlEbhHE8vYXlF6K5xGZ2rdOrn3cQ-LnQ",
            "y": "9Z_l_hQLkq6aLuZz8gheq7R_o5ZUHUlxZ3IBGHsdzaA"
            }
        }
        ],
        "service": [
        {
            "id": "did:elsi:VATES-B60645900#info",
            "type": "EntityCommercialInfo",
            "serviceEndpoint": "www.in2.es",
            "name": "IN2 Innovating 2gether"
        },
        {
            "id": "did:elsi:VATES-B60645900#sms",
            "type": "SecureMessagingService",
            "serviceEndpoint": "https://privatecred.hesusruiz.org/api"
        }
        ],
        "anchors": [
        {
            "id": "redt.alastria",
            "resolution": "UniversalResolver",
            "domain": "in2.ala",
            "ethereumAddress": "0x8CDA8113567e633805e48c87747257E9FFAAdDF5"
        }
        ],
        "created": "2021-02-08T06:53:08Z",
        "updated": "2021-02-08T06:53:08Z"
    }
    }


