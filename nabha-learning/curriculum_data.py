# -*- coding: utf-8 -*-
"""Starter curriculum for Classes 5-10 (6 subjects per class).

Structure: CURRICULUM[class_number] = [ (subject_title, description, [ (unit_title, unit_content), ... ]), ... ]
Teachers can extend or edit this content later; seeding only adds subjects that do not exist yet.
"""

CURRICULUM = {
    # ------------------------------------------------------------------ CLASS 5
    5: [
        ("Mathematics", "Numbers, fractions and measurement for everyday life.", [
            ("Place Value and Large Numbers",
             "We use the Indian place-value system: ones, tens, hundreds, thousands, ten-thousands, lakhs, ten-lakhs and crores.\n"
             "• 4,56,328 is read as four lakh fifty-six thousand three hundred twenty-eight.\n"
             "• To compare two numbers, first count the digits (more digits = bigger number). If the digits are equal, compare from the left.\n"
             "• Rounding to the nearest ten: look at the ones digit. 5 or more, round up; 4 or less, round down. 67 becomes 70."),
            ("Fractions",
             "A fraction shows part of a whole. In 3/4, the numerator (3) is the parts we take and the denominator (4) is the total equal parts.\n"
             "• Like fractions (same denominator): add the numerators. 2/7 + 3/7 = 5/7.\n"
             "• Unlike fractions: make the denominators equal first. 1/2 + 1/3 = 3/6 + 2/6 = 5/6.\n"
             "• Equivalent fractions have the same value: 1/2 = 2/4 = 3/6."),
            ("Perimeter and Area",
             "Perimeter is the distance around a shape. Area is the space inside it.\n"
             "• Rectangle: Perimeter = 2 × (length + breadth); Area = length × breadth.\n"
             "• Square: Perimeter = 4 × side; Area = side × side.\n"
             "• Example: a field 8 m long and 5 m wide has perimeter 2 × (8 + 5) = 26 m and area 8 × 5 = 40 square metres."),
        ]),
        ("English", "Grammar, reading and writing skills.", [
            ("Nouns and Pronouns",
             "A noun names a person, place, animal or thing. Common nouns are general (girl, city). Proper nouns name something specific and start with a capital letter (Simran, Nabha).\n"
             "A pronoun takes the place of a noun: I, you, he, she, it, we, they.\n"
             "• Ravi is tall. He plays football. ('He' replaces 'Ravi'.)"),
            ("Verbs and Simple Tenses",
             "A verb tells what someone does or is. Tense tells us when.\n"
             "• Present: She reads a book.\n"
             "• Past: She read a book yesterday.\n"
             "• Future: She will read a book tomorrow.\n"
             "Tip: for 'he/she/it' in the simple present, add -s or -es (he plays, she watches)."),
            ("Writing a Paragraph and a Letter",
             "A good paragraph has a topic sentence, three or four supporting sentences and a closing sentence.\n"
             "A friendly letter has: your address and date, greeting (Dear Amit,), body, closing (Your friend,) and your name.\n"
             "Practise: write five sentences about your school."),
        ]),
        ("EVS", "Environmental Studies: our surroundings, water, food and health.", [
            ("Water - Our Lifeline",
             "All living things need water. Sources of water include rain, rivers, ponds, wells and tube wells.\n"
             "• Water is safe to drink only when it is clean. Boiling for several minutes or filtering makes it safer.\n"
             "• Save water: close the tap while brushing, reuse water for plants, fix leaking taps.\n"
             "• Punjab depends heavily on groundwater, so saving water matters for our farms."),
            ("Plants and Animals Around Us",
             "Plants make their own food using sunlight. Animals depend on plants or other animals for food.\n"
             "• Herbivores eat plants (cow), carnivores eat animals (lion), omnivores eat both (crow).\n"
             "• A food chain shows who eats whom: grass -> grasshopper -> frog -> snake."),
            ("Food and Good Health",
             "A balanced diet includes cereals (energy), pulses (body-building protein), fruits and vegetables (vitamins and minerals) and milk products.\n"
             "• Wash hands before eating and after using the toilet.\n"
             "• Drink safe water, sleep 8-10 hours and play outdoors every day."),
        ]),
        ("Science", "Simple ideas about matter, space and machines.", [
            ("States of Matter",
             "Matter is anything that has weight and takes up space. It exists in three states.\n"
             "• Solid: has fixed shape and size (stone).\n"
             "• Liquid: has fixed volume but no fixed shape (water).\n"
             "• Gas: has neither fixed shape nor volume (air).\n"
             "Water can change state: ice melts to water, and water boils to steam."),
            ("The Solar System",
             "The Sun is a star at the centre of our solar system. Eight planets move around it: Mercury, Venus, Earth, Mars, Jupiter, Saturn, Uranus and Neptune.\n"
             "• Earth is the only planet known to have life.\n"
             "• The Moon is Earth's natural satellite. It shines by reflecting sunlight.\n"
             "• Earth takes 24 hours to rotate once (day and night) and about 365 days to go around the Sun."),
            ("Simple Machines",
             "Simple machines make work easier.\n"
             "• Lever: a bar that turns on a fixed point (see-saw, scissors).\n"
             "• Inclined plane: a slope that helps lift loads (a ramp).\n"
             "• Pulley: a wheel with a rope, used to lift water from a well.\n"
             "• Wheel and axle: makes things roll easily (cart, bicycle)."),
        ]),
        ("Social Studies", "Our country, our government and our state.", [
            ("Our Country - India",
             "India is a large country in South Asia with 28 states and several union territories. Its capital is New Delhi.\n"
             "• Our national symbols: the Tricolour flag, the Lion Capital emblem, the national anthem and the national song.\n"
             "• India has many languages, festivals and foods, yet we are one nation - this is 'Unity in Diversity'."),
            ("Local Government - Panchayati Raj",
             "Villages are governed by the Gram Panchayat, led by the Sarpanch, who is elected by the villagers.\n"
             "• The Panchayat looks after drinking water, roads, street lights, schools and cleanliness.\n"
             "• Towns are managed by a Municipal Council or Corporation."),
            ("Punjab - Our State",
             "Punjab is in north-west India. Its capital is Chandigarh. The name means 'land of five rivers'.\n"
             "• Punjab is called the 'granary of India' because of its wheat and rice.\n"
             "• Nabha is a historic town in Punjab, once the capital of the princely state of Nabha.\n"
             "• Punjabi is the main language, and Baisakhi and Lohri are popular festivals."),
        ]),
        ("Hindi", "हिंदी व्याकरण और लेखन।", [
            ("संज्ञा (Noun)",
             "किसी व्यक्ति, स्थान, वस्तु या भाव के नाम को संज्ञा कहते हैं।\n"
             "• व्यक्तिवाचक संज्ञा: राम, पंजाब, गंगा।\n"
             "• जातिवाचक संज्ञा: लड़का, शहर, नदी।\n"
             "• भाववाचक संज्ञा: सुंदरता, ईमानदारी, बचपन।"),
            ("सर्वनाम (Pronoun)",
             "संज्ञा के स्थान पर आने वाले शब्द को सर्वनाम कहते हैं।\n"
             "• उदाहरण: मैं, तुम, वह, हम, आप, यह।\n"
             "• वाक्य: सीता स्कूल गई। वह पढ़ती है। (यहाँ 'वह' सर्वनाम है।)"),
            ("क्रिया (Verb)",
             "जिस शब्द से किसी काम का करना या होना पता चले उसे क्रिया कहते हैं।\n"
             "• उदाहरण: खाना, पढ़ना, खेलना, दौड़ना।\n"
             "• काल के तीन भेद हैं: भूतकाल (वह गया), वर्तमान काल (वह जाता है), भविष्यत् काल (वह जाएगा)।"),
        ]),
    ],

    # ------------------------------------------------------------------ CLASS 6
    6: [
        ("Mathematics", "Number play, integers and the first steps in algebra.", [
            ("Playing with Numbers",
             "A factor divides a number exactly; a multiple is obtained by multiplying.\n"
             "• Factors of 12: 1, 2, 3, 4, 6, 12.\n"
             "• A prime number has exactly two factors, 1 and itself (2, 3, 5, 7, 11). A composite number has more than two.\n"
             "• HCF = highest common factor; LCM = lowest common multiple. For 12 and 18: HCF = 6, LCM = 36.\n"
             "• Divisibility: a number is divisible by 3 if the sum of its digits is divisible by 3."),
            ("Integers",
             "Integers are ..., -3, -2, -1, 0, 1, 2, 3, ... They include negative numbers, zero and positive numbers.\n"
             "• On a number line, numbers increase to the right.\n"
             "• Adding a negative is the same as subtracting: 5 + (-3) = 2.\n"
             "• Example: a temperature of -4 degrees is lower than -1 degree."),
            ("Introduction to Algebra",
             "Algebra uses letters (variables) for unknown numbers.\n"
             "• If a pencil costs Rs. 5, then n pencils cost 5n rupees.\n"
             "• An equation such as x + 7 = 12 is solved by doing the same thing on both sides: x = 12 - 7 = 5.\n"
             "• Always check by putting the answer back: 5 + 7 = 12."),
        ]),
        ("English", "Grammar, tenses and writing.", [
            ("Adjectives and Adverbs",
             "An adjective describes a noun (a tall boy, red apples). An adverb describes a verb, adjective or another adverb and often ends in -ly (she walks slowly).\n"
             "Degrees of comparison: tall -> taller -> tallest; good -> better -> best."),
            ("Tenses",
             "Each tense has simple, continuous and perfect forms.\n"
             "• Simple present: I write.\n"
             "• Present continuous: I am writing.\n"
             "• Present perfect: I have written.\n"
             "• Simple past: I wrote.\n"
             "• Simple future: I will write."),
            ("Letter and Paragraph Writing",
             "In a formal letter to the Principal: write the sender's address, date, 'To', subject line, 'Sir/Madam', the body, 'Yours obediently' and your name.\n"
             "In a paragraph keep to one idea, use linking words (first, then, finally) and check spelling and punctuation."),
        ]),
        ("Physics", "Measurement, motion, light and electricity.", [
            ("Motion and Measurement",
             "To measure length we compare it with a standard unit. The SI unit of length is the metre (m).\n"
             "• Use a metre scale or measuring tape. Keep your eye directly above the mark to avoid error.\n"
             "• Motion types: rectilinear (a car on a straight road), circular (a ceiling fan), periodic (a swing).\n"
             "• Speed = distance / time. A bus covering 120 km in 2 hours has speed 60 km/h."),
            ("Light, Shadows and Reflection",
             "Light travels in straight lines. Objects can be transparent (glass), translucent (butter paper) or opaque (wood).\n"
             "• A shadow forms when an opaque object blocks light.\n"
             "• A plane mirror forms an image of the same size, as far behind the mirror as the object is in front.\n"
             "• The Sun and a bulb are luminous (they give out light); the Moon is not."),
            ("Electricity and Circuits",
             "An electric cell supplies electricity. A bulb glows when there is a closed circuit: cell, wires, switch and bulb joined in a complete loop.\n"
             "• Conductors (copper, iron, aluminium) allow current to pass; insulators (rubber, plastic, wood) do not.\n"
             "• Never touch switches with wet hands, and never put metal objects into sockets."),
        ]),
        ("Chemistry", "Materials, separation and changes.", [
            ("Sorting Materials",
             "Materials are grouped by their properties such as appearance, hardness, solubility in water and whether they float or sink.\n"
             "• Lustrous materials shine (metals).\n"
             "• Soluble materials dissolve in water (sugar, salt); insoluble ones do not (sand, chalk).\n"
             "• Transparent, translucent and opaque describe how much light passes through."),
            ("Separation of Substances",
             "Mixtures can be separated by simple methods.\n"
             "• Handpicking: removing stones from rice.\n"
             "• Winnowing: separating husk from grain using wind.\n"
             "• Sieving: separating wheat flour from bran.\n"
             "• Filtration: removing sand from water.\n"
             "• Evaporation: getting salt from salt solution.\n"
             "• Sedimentation and decantation: letting heavy particles settle, then pouring off the liquid."),
            ("Changes Around Us",
             "A physical change does not form a new substance (melting ice, tearing paper). It can often be reversed.\n"
             "A chemical change forms a new substance and is usually permanent (burning wood, rusting of iron, curdling of milk).\n"
             "Rusting needs both oxygen and water; painting or oiling iron protects it."),
        ]),
        ("Biology", "Food, plants and the human body.", [
            ("Components of Food",
             "Food contains carbohydrates and fats (energy), proteins (growth and repair), vitamins and minerals (protection from disease), water and roughage (fibre).\n"
             "• Deficiency diseases: lack of Vitamin C causes scurvy; lack of Vitamin D causes rickets; lack of iron causes anaemia; lack of iodine causes goitre.\n"
             "• A balanced diet contains all the components in the right amount."),
            ("Getting to Know Plants",
             "Plants have roots, stem, leaves, flowers and fruits.\n"
             "• Roots absorb water and minerals; the stem carries them upward.\n"
             "• Leaves make food by photosynthesis using sunlight, water and carbon dioxide, and release oxygen.\n"
             "• Plants can be herbs (small, soft stem), shrubs, or trees (tall, hard woody stem)."),
            ("Body Movements",
             "The human skeleton has 206 bones in adults. It gives shape, protects organs and helps movement.\n"
             "• Joints let bones move: ball-and-socket (shoulder), hinge (elbow, knee), pivot (neck), fixed (skull).\n"
             "• Muscles pull on bones to produce movement."),
        ]),
        ("Social Science", "History, geography and civics together.", [
            ("History - Earliest Humans",
             "Early humans were hunter-gatherers who lived in caves, made stone tools and discovered fire.\n"
             "• Later they learned farming and kept animals, so they settled in villages (the Neolithic age).\n"
             "• The Harappan (Indus Valley) civilisation had well-planned cities such as Mohenjo-daro and Harappa. Rakhigarhi in Haryana is another large site."),
            ("Geography - The Earth",
             "The Earth is the third planet from the Sun and is slightly flattened at the poles.\n"
             "• The globe is a model of the Earth. The Equator (0 degrees latitude) divides it into the Northern and Southern Hemispheres.\n"
             "• The Prime Meridian (0 degrees longitude) passes through Greenwich.\n"
             "• Earth has seven continents: Asia, Africa, North America, South America, Antarctica, Europe and Australia."),
            ("Civics - Diversity and Democracy",
             "India has people of many religions, languages and cultures. Diversity makes the country rich, and we must respect everyone.\n"
             "In a democracy citizens vote to choose their government. Every Indian citizen aged 18 or above has the right to vote."),
        ]),
    ],

    # ------------------------------------------------------------------ CLASS 7
    7: [
        ("Geography", "Our environment and the earth.", [
            ("Environment",
             "The environment is everything around us: natural (land, water, air, plants, animals) and human-made (buildings, roads, machines).\n"
             "• Its main parts are the lithosphere (land), hydrosphere (water), atmosphere (air) and biosphere (all living things).\n"
             "• Humans change the environment, so we must protect it by planting trees and reducing waste."),
            ("Inside Our Earth",
             "The Earth has layers: the crust (outer, thin), the mantle (middle) and the core (centre, made mostly of nickel and iron).\n"
             "• Rocks are of three kinds: igneous (from cooled magma), sedimentary (layers of deposits) and metamorphic (changed by heat and pressure).\n"
             "• Minerals such as iron, coal and limestone are found in rocks and are used in industry."),
            ("Air - The Atmosphere",
             "The atmosphere is the layer of gases around the Earth. It is about 78% nitrogen and 21% oxygen.\n"
             "• Its layers from the ground upwards: troposphere (weather happens here), stratosphere (ozone layer), mesosphere, thermosphere, exosphere.\n"
             "• Wind is moving air. Air pressure is the weight of air on a surface; warm air rises and cold air sinks."),
        ]),
        ("History", "Medieval India.", [
            ("The Delhi Sultanate",
             "In 1206 Qutbuddin Aibak founded the Delhi Sultanate, which was ruled by five dynasties until 1526.\n"
             "• Famous rulers include Iltutmish, Razia Sultan (the first woman ruler of Delhi), Alauddin Khalji and Muhammad bin Tughlaq.\n"
             "• The Qutub Minar in Delhi was begun under Aibak and completed by Iltutmish."),
            ("The Mughal Empire",
             "Babur founded the Mughal Empire after winning the First Battle of Panipat in 1526.\n"
             "• Akbar (ruled 1556-1605) expanded the empire and followed a policy of religious tolerance.\n"
             "• Shah Jahan built the Taj Mahal at Agra and the Red Fort at Delhi. Aurangzeb ruled after him.\n"
             "• Mughal administration used the mansabdari system to rank officers."),
            ("Regional Kingdoms and Bhakti-Sufi Movements",
             "The Vijayanagara Empire (1336 onward) in south India was known for its capital Hampi.\n"
             "Bhakti saints such as Kabir and Guru Nanak taught devotion and equality. Guru Nanak (1469-1539), born in Punjab, founded Sikhism and taught 'Naam Japo, Kirat Karo, Vand Chhako'."),
        ]),
        ("Civics", "Equality, health and state government.", [
            ("On Equality",
             "Equality means every person is valued equally, regardless of caste, religion, gender, wealth or ability.\n"
             "• The Indian Constitution gives everyone the Right to Equality and bans untouchability.\n"
             "• Every adult citizen has one vote, and every vote has equal value (universal adult franchise)."),
            ("Role of the Government in Health",
             "Good health care should reach everyone. India has both public (government) and private health services.\n"
             "• Government hospitals and health centres provide low-cost care and run vaccination programmes.\n"
             "• Clean water, nutrition and sanitation also keep people healthy."),
            ("How the State Government Works",
             "Each state has a Legislative Assembly (Vidhan Sabha) whose members are called MLAs.\n"
             "• The party with majority forms the government and its leader becomes Chief Minister.\n"
             "• The Governor is the head of the state and is appointed by the President.\n"
             "• Ministers run departments such as health, education and agriculture."),
        ]),
        ("Mathematics", "Integers, equations and triangles.", [
            ("Integers",
             "Rules for operations on integers:\n"
             "• Same signs add: (-3) + (-4) = -7.\n"
             "• Different signs subtract and take the sign of the larger: 8 + (-5) = 3.\n"
             "• Multiplication: positive x positive = positive; negative x negative = positive; positive x negative = negative.\n"
             "• Example: (-6) x (-2) = 12; (-6) x 2 = -12."),
            ("Simple Equations",
             "An equation says two expressions are equal. To solve it, do the same operation on both sides.\n"
             "• Solve 3x + 5 = 20: subtract 5 -> 3x = 15; divide by 3 -> x = 5.\n"
             "• Word problem: a number increased by 9 is 25. x + 9 = 25, so x = 16."),
            ("Triangles and Their Properties",
             "The three angles of any triangle add up to 180 degrees.\n"
             "• Types by sides: equilateral (3 equal), isosceles (2 equal), scalene (none equal).\n"
             "• Types by angles: acute, right (one 90 degree angle), obtuse.\n"
             "• Pythagoras theorem for right triangles: (hypotenuse)^2 = (side1)^2 + (side2)^2. For sides 3 and 4, hypotenuse = 5."),
        ]),
        ("English", "Voice, speech and writing.", [
            ("Active and Passive Voice",
             "In active voice the subject does the action: Ravi writes a letter.\n"
             "In passive voice the action is done to the subject: A letter is written by Ravi.\n"
             "Passive = object + form of 'be' + past participle (+ by + doer)."),
            ("Direct and Indirect Speech",
             "Direct: She said, 'I am tired.'\n"
             "Indirect: She said that she was tired.\n"
             "Changes: remove the quotation marks, add 'that', change the pronoun and move the tense one step back (am -> was, will -> would)."),
            ("Notice and Essay Writing",
             "A notice has: the name of the institution, the word NOTICE, date, heading, short body (what, when, where), and the name and designation of the writer.\n"
             "An essay has an introduction, a body of two or three paragraphs and a conclusion."),
        ]),
        ("Science", "Plants, heat and acids.", [
            ("Nutrition in Plants",
             "Green plants make their own food by photosynthesis: carbon dioxide + water --(sunlight, chlorophyll)--> glucose + oxygen.\n"
             "• Chlorophyll is the green pigment in leaves.\n"
             "• Some plants are not green and depend on others: parasites (cuscuta), insectivorous plants (pitcher plant)."),
            ("Heat",
             "Temperature tells how hot or cold something is. It is measured in degrees Celsius with a thermometer. Normal human body temperature is about 37 degrees Celsius.\n"
             "• Conduction: heat flows through solids (a spoon in hot tea).\n"
             "• Convection: heat flows in liquids and gases (boiling water).\n"
             "• Radiation: heat travels without any medium (heat from the Sun)."),
            ("Acids, Bases and Salts",
             "Acids taste sour (lemon, vinegar) and turn blue litmus red. Bases taste bitter and feel soapy; they turn red litmus blue.\n"
             "• Neutralisation: acid + base -> salt + water. An antacid tablet neutralises excess stomach acid.\n"
             "• Indicators such as litmus, turmeric and china rose show whether a substance is acidic or basic."),
        ]),
    ],

    # ------------------------------------------------------------------ CLASS 8
    8: [
        ("Mathematics", "Rational numbers, equations and mensuration.", [
            ("Rational Numbers",
             "A rational number can be written as p/q where p and q are integers and q is not zero. Examples: 3/4, -5/2, 7 (= 7/1).\n"
             "• Properties: closure, commutativity and associativity hold for addition and multiplication.\n"
             "• 0 is the additive identity and 1 is the multiplicative identity.\n"
             "• Between any two rational numbers there are infinitely many rational numbers."),
            ("Linear Equations in One Variable",
             "To solve: move variable terms to one side and numbers to the other.\n"
             "• Solve 2x - 3 = x + 5: x = 8.\n"
             "• Word problem: the sum of two consecutive numbers is 41. Let the numbers be x and x + 1; 2x + 1 = 41, so x = 20; numbers are 20 and 21."),
            ("Mensuration",
             "• Area of trapezium = 1/2 x (sum of parallel sides) x height.\n"
             "• Surface area of a cuboid = 2(lb + bh + hl); volume = l x b x h.\n"
             "• Surface area of a cube = 6a^2; volume = a^3.\n"
             "• Volume of a cylinder = pi x r^2 x h.\n"
             "Example: a cube of side 3 cm has volume 27 cubic cm."),
        ]),
        ("English", "Grammar and communication.", [
            ("Subject-Verb Agreement and Tenses",
             "The verb must agree with the subject in number.\n"
             "• He goes / They go.\n"
             "• Each of the boys is present. (each, every, neither take singular verbs)\n"
             "Use perfect continuous tenses for actions that started earlier and continue: She has been studying since morning."),
            ("Formal Letters and Emails",
             "A formal email has a clear subject line, a polite greeting (Dear Sir/Madam), a short body that states the purpose, a courteous closing (Yours faithfully) and your name and contact.\n"
             "Use simple, polite and precise language. Avoid slang."),
            ("Reading and Summary Writing",
             "To summarise: read the passage twice, underline the main ideas, write them in your own words in about one-third of the original length, and do not add your own opinion."),
        ]),
        ("Science", "Crops, cells and force.", [
            ("Crop Production and Management",
             "Crops are of two main seasons: Kharif (sown with the monsoon in June-July: rice, maize, cotton) and Rabi (sown in winter in October-November: wheat, gram, mustard).\n"
             "• Steps: preparing the soil, sowing, adding manure and fertiliser, irrigation, weeding, harvesting and storage.\n"
             "• Wheat and paddy are the main crops of Punjab."),
            ("Cell - Structure and Functions",
             "The cell is the basic unit of life, discovered by Robert Hooke in 1665.\n"
             "• Parts: cell membrane, cytoplasm and nucleus (the control centre).\n"
             "• Plant cells also have a cell wall, large vacuoles and chloroplasts.\n"
             "• Unicellular organisms (amoeba) have one cell; multicellular organisms (humans) have many."),
            ("Force and Pressure",
             "A force is a push or a pull. It can change the speed, direction or shape of an object.\n"
             "• Friction is the force that opposes motion between surfaces.\n"
             "• Pressure = force / area. A sharp knife cuts easily because a small area gives high pressure.\n"
             "• Atmospheric pressure acts on everything on Earth."),
        ]),
        ("History", "The British period and the freedom struggle.", [
            ("From Trade to Territory",
             "The British East India Company came to India for trade. After the Battle of Plassey (1757) and the Battle of Buxar (1764) it gained political control of Bengal.\n"
             "• Robert Clive led the Company at Plassey.\n"
             "• The Company expanded through wars and policies like the Subsidiary Alliance."),
            ("The Revolt of 1857",
             "The Revolt of 1857 began at Meerut on 10 May 1857 when Indian soldiers (sepoys) rose against the Company.\n"
             "• Leaders: Rani Lakshmibai, Tantia Tope, Nana Sahib, Bahadur Shah Zafar.\n"
             "• After it the rule of the Company ended and India came directly under the British Crown (1858)."),
            ("The Beginning of the National Movement",
             "The Indian National Congress was founded in 1885.\n"
             "• Mahatma Gandhi led movements of non-violence (satyagraha), including Non-Cooperation, Dandi March and Quit India (1942).\n"
             "• India became independent on 15 August 1947."),
        ]),
        ("Geography", "Resources, agriculture and industries.", [
            ("Resources",
             "A resource is anything useful to people. Natural resources (water, soil, minerals) come from nature; human-made resources include roads and machines.\n"
             "• Renewable resources (solar, wind, water) can be replenished. Non-renewable ones (coal, petroleum) will run out.\n"
             "• Sustainable use means saving resources for future generations."),
            ("Agriculture",
             "Farming systems: subsistence (for the family) and commercial (for sale).\n"
             "• Major crops: rice, wheat, millets, pulses, sugarcane, cotton, tea and coffee.\n"
             "• Punjab and Haryana lead wheat production because of fertile alluvial soil and canal and tube-well irrigation.\n"
             "• The Green Revolution of the 1960s raised yields using high-yielding seeds."),
            ("Industries",
             "Industries turn raw materials into finished goods.\n"
             "• Agro-based (cotton textile, sugar), mineral-based (iron and steel), and small-scale or cottage industries.\n"
             "• Industries need raw materials, power, labour, capital and markets."),
        ]),
        ("Civics", "The Constitution and government.", [
            ("The Indian Constitution",
             "The Constitution was adopted on 26 November 1949 and came into force on 26 January 1950. Dr B. R. Ambedkar chaired its Drafting Committee.\n"
             "• Fundamental Rights include equality, freedom, protection from exploitation, freedom of religion, cultural and educational rights and the right to constitutional remedies.\n"
             "• Citizens also have Fundamental Duties."),
            ("Parliament and the Making of Laws",
             "Parliament has the President, the Lok Sabha (House of the People) and the Rajya Sabha (Council of States).\n"
             "• Members of Lok Sabha are elected directly by the people.\n"
             "• A bill becomes a law after both Houses pass it and the President gives assent."),
            ("The Judiciary",
             "The judiciary interprets laws and settles disputes. Its levels are the Supreme Court, High Courts and District Courts.\n"
             "• Judges are independent so they can decide without pressure.\n"
             "• Everyone, including the government, must obey the law."),
        ]),
        ("Telugu (2nd Language)", "తెలుగు వ్యాకరణం మరియు రచన - Telugu as a second language.", [
            ("తెలుగు వర్ణమాల (Telugu Alphabet)",
             "తెలుగు భాషలో అచ్చులు, హల్లులు మరియు ఉభయాక్షరాలు ఉంటాయి.\n"
             "• అచ్చులు (Vowels): అ, ఆ, ఇ, ఈ, ఉ, ఊ, ఋ, ఎ, ఏ, ఐ, ఒ, ఓ, ఔ.\n"
             "• హల్లులు (Consonants): క, ఖ, గ, ఘ, ఙ, చ, ఛ, జ, ఝ, ఞ ... మొదలైనవి.\n"
             "• ఉదాహరణ: అమ్మ, నాన్న, పుస్తకం, బడి."),
            ("నామవాచకం మరియు సర్వనామం (Noun and Pronoun)",
             "ఒక వ్యక్తి, వస్తువు, ప్రదేశం పేరును తెలిపే పదాన్ని నామవాచకం అంటారు.\n"
             "• ఉదాహరణ: రాముడు, నది, హైదరాబాద్, పుస్తకం.\n"
             "• నామవాచకానికి బదులుగా వాడే పదాన్ని సర్వనామం అంటారు: నేను, నువ్వు, అతడు, ఆమె, మేము, వారు.\n"
             "• వాక్యం: సీత బడికి వెళ్ళింది. ఆమె బాగా చదువుతుంది. (ఇక్కడ 'ఆమె' సర్వనామం.)"),
            ("క్రియ మరియు కాలాలు (Verb and Tenses)",
             "పనిని తెలిపే పదాన్ని క్రియ అంటారు. ఉదాహరణ: తినడం, చదవడం, ఆడటం, పరుగెత్తడం.\n"
             "• భూతకాలం (Past): అతడు వెళ్ళాడు.\n"
             "• వర్తమానకాలం (Present): అతడు వెళ్తున్నాడు.\n"
             "• భవిష్యత్తు కాలం (Future): అతడు వెళ్తాడు."),
            ("సామెతలు మరియు పద్యాలు (Proverbs and Poems)",
             "సామెతలు తక్కువ మాటల్లో గొప్ప అర్థాన్ని చెబుతాయి.\n"
             "• 'తిన్నింటి వాసాలు లెక్కపెట్టకూడదు' - మేలు చేసిన వారికి కీడు చేయకూడదు.\n"
             "• 'అభ్యాసం కూసువిద్య' - సాధనతోనే విద్య అబ్బుతుంది.\n"
             "• తెలుగు పద్యాలు వేమన, సుమతీ శతకాలలో నీతిని బోధిస్తాయి."),
            ("లేఖ మరియు వ్యాస రచన (Letter and Essay Writing)",
             "లేఖలో తేదీ, సంబోధన, విషయం, ముగింపు మరియు సంతకం ఉండాలి.\n"
             "• స్నేహితునికి లేఖ రాసేటప్పుడు 'ప్రియమైన మిత్రునికి' అని ప్రారంభించాలి.\n"
             "• వ్యాసంలో ప్రారంభం, విషయ వివరణ మరియు ముగింపు అనే మూడు భాగాలు ఉంటాయి.\n"
             "• సరళమైన, స్పష్టమైన భాషను వాడాలి."),
        ]),
    ],

    # ------------------------------------------------------------------ CLASS 9
    9: [
        ("Mathematics", "Number systems, polynomials and geometry.", [
            ("Number Systems",
             "Natural numbers N, whole numbers W, integers Z, rational numbers Q (p/q form) and irrational numbers (cannot be written as p/q, with non-repeating non-terminating decimals).\n"
             "• Examples of irrational numbers: square root of 2, square root of 3, pi.\n"
             "• Real numbers = rational + irrational numbers; each real number is a point on the number line.\n"
             "• Laws of exponents: a^m x a^n = a^(m+n); (a^m)^n = a^(mn)."),
            ("Polynomials",
             "A polynomial in x is an expression such as 3x^2 - 5x + 2. Its degree is the highest power of x.\n"
             "• A zero of p(x) is a value k with p(k) = 0.\n"
             "• Remainder Theorem: when p(x) is divided by (x - a), the remainder is p(a).\n"
             "• Factor Theorem: (x - a) is a factor of p(x) if p(a) = 0.\n"
             "• Identity: (a + b)^2 = a^2 + 2ab + b^2."),
            ("Lines and Angles",
             "• Angles on a straight line add up to 180 degrees (linear pair).\n"
             "• Vertically opposite angles are equal.\n"
             "• If a transversal cuts two parallel lines, corresponding angles are equal and alternate interior angles are equal.\n"
             "• The sum of the angles of a triangle is 180 degrees."),
        ]),
        ("English", "Grammar and writing for the secondary stage.", [
            ("Modals and Their Uses",
             "Modals (can, could, may, might, shall, should, will, would, must) express ability, permission, possibility, advice or obligation.\n"
             "• You should drink more water (advice).\n"
             "• May I come in? (permission)\n"
             "• He must wear a helmet (obligation)."),
            ("Writing Skills - Letters and Articles",
             "Formal letters (to the editor, to officials) need a clear subject, facts and a polite tone.\n"
             "An article has a catchy title, the writer's name, an introduction, two or three paragraphs of development and a conclusion."),
            ("Reading Comprehension",
             "Read the passage fully first, then the questions. Find the answer in the passage and write it in your own words. For vocabulary questions, use context clues around the word."),
        ]),
        ("Physics", "Motion, force and gravitation.", [
            ("Motion",
             "Distance is the path length; displacement is the shortest straight distance between start and end points. Speed = distance / time; velocity = displacement / time.\n"
             "Equations of uniformly accelerated motion:\n"
             "• v = u + at\n"
             "• s = ut + (1/2)at^2\n"
             "• v^2 = u^2 + 2as\n"
             "Example: a car starting from rest (u = 0) with a = 2 m/s^2 for 5 s reaches v = 10 m/s."),
            ("Force and Laws of Motion",
             "Newton's laws:\n"
             "• First law (inertia): an object stays at rest or in uniform motion unless a force acts on it.\n"
             "• Second law: F = ma. Force equals mass times acceleration.\n"
             "• Third law: every action has an equal and opposite reaction (a rocket moving up, a gun recoiling).\n"
             "The SI unit of force is the newton (N)."),
            ("Gravitation",
             "Universal law of gravitation: F = G m1 m2 / r^2, where G = 6.67 x 10^-11 N m^2/kg^2.\n"
             "• Acceleration due to gravity near Earth's surface g = 9.8 m/s^2.\n"
             "• Mass is the amount of matter (kg) and is the same everywhere; weight = mg and changes with g (the Moon's gravity is about one-sixth of the Earth's).\n"
             "• Objects float when the buoyant force balances their weight (Archimedes' principle)."),
        ]),
        ("Chemistry", "Matter and the atom.", [
            ("Matter in Our Surroundings",
             "Matter exists as solid, liquid or gas. Changes of state occur by changing temperature or pressure.\n"
             "• Melting point of ice = 0 degrees C (273 K); boiling point of water = 100 degrees C (373 K).\n"
             "• Evaporation is a surface phenomenon and causes cooling; sweating cools our body.\n"
             "• Kelvin = Celsius + 273."),
            ("Atoms and Molecules",
             "Law of conservation of mass: mass is neither created nor destroyed in a chemical reaction.\n"
             "Law of constant proportions: a compound always contains the same elements in the same ratio by mass (water: hydrogen and oxygen in 1:8 by mass).\n"
             "• A molecule is formed by two or more atoms (O2, H2O).\n"
             "• One mole of a substance contains 6.022 x 10^23 particles (Avogadro number)."),
            ("Structure of the Atom",
             "An atom has a nucleus containing protons (positive) and neutrons (neutral), with electrons (negative) moving around it.\n"
             "• Atomic number = number of protons; mass number = protons + neutrons.\n"
             "• Bohr's model: electrons are in shells with maximum 2, 8, 18 electrons (K, L, M).\n"
             "• Isotopes have the same atomic number but different mass numbers (carbon-12 and carbon-14)."),
        ]),
        ("Biology", "Cells, tissues and health.", [
            ("The Fundamental Unit of Life - The Cell",
             "All living things are made of cells. Cell organelles and their functions:\n"
             "• Nucleus: controls the cell and holds DNA.\n"
             "• Mitochondria: the 'powerhouse', release energy.\n"
             "• Ribosomes: make proteins.\n"
             "• Endoplasmic reticulum and Golgi apparatus: transport and packaging.\n"
             "• Plastids (chloroplasts): photosynthesis in plant cells.\n"
             "Prokaryotic cells (bacteria) have no true nucleus; eukaryotic cells do."),
            ("Tissues",
             "A tissue is a group of similar cells doing a particular job.\n"
             "• Plant tissues: meristematic (growth) and permanent (xylem carries water; phloem carries food).\n"
             "• Animal tissues: epithelial (covering), connective (blood, bone), muscular (movement) and nervous (messages)."),
            ("Why Do We Fall Ill?",
             "Health is a state of physical, mental and social well-being.\n"
             "• Diseases may be infectious (caused by bacteria, viruses, protozoa: typhoid, influenza, malaria) or non-infectious.\n"
             "• Prevention: clean water, hygiene, vaccination and removing stagnant water where mosquitoes breed.\n"
             "• Antibiotics work on bacteria, not on viruses."),
        ]),
        ("Economics", "The village economy, people and poverty.", [
            ("The Story of Village Palampur",
             "Farming is the main activity in Palampur. Four factors of production are needed: land, labour, physical capital (tools, machines, seeds) and human capital (knowledge and skill).\n"
             "• Land is fixed, so farmers use multiple cropping to grow more from the same land.\n"
             "• Non-farm activities such as dairy, small manufacturing and shops give additional income."),
            ("People as Resource",
             "People become a resource when they are educated and healthy. Education and health improve human capital.\n"
             "• Economic activities are of three sectors: primary (agriculture), secondary (industry) and tertiary (services).\n"
             "• Unemployment includes disguised unemployment, when more people work on a farm than needed."),
            ("Poverty as a Challenge",
             "Poverty means lack of basic needs such as food, clothing and shelter.\n"
             "• The poverty line is the minimum income or consumption needed to meet basic needs.\n"
             "• Causes include low income, unemployment, illiteracy and inequality.\n"
             "• Government schemes like the Mahatma Gandhi NREGA give 100 days of wage employment in rural areas."),
        ]),
    ],

    # ------------------------------------------------------------------ CLASS 10
    10: [
        ("Mathematics", "Board-level algebra and trigonometry basics.", [
            ("Real Numbers",
             "Euclid's division lemma: for positive integers a and b, a = bq + r with 0 <= r < b.\n"
             "• Fundamental Theorem of Arithmetic: every composite number can be written as a product of primes in a unique way.\n"
             "• For two positive integers a and b: HCF(a, b) x LCM(a, b) = a x b.\n"
             "• Example: for 12 and 18, HCF = 6, LCM = 36 and 6 x 36 = 216 = 12 x 18."),
            ("Quadratic Equations",
             "A quadratic equation is ax^2 + bx + c = 0 with a not equal to 0.\n"
             "• Quadratic formula: x = (-b +/- sqrt(b^2 - 4ac)) / 2a.\n"
             "• Discriminant D = b^2 - 4ac. If D > 0, two distinct real roots; D = 0, equal roots; D < 0, no real roots.\n"
             "• Example: x^2 - 5x + 6 = 0 factorises as (x - 2)(x - 3) = 0, so x = 2 or 3."),
            ("Introduction to Trigonometry",
             "In a right triangle with angle theta: sin = opposite/hypotenuse, cos = adjacent/hypotenuse, tan = opposite/adjacent.\n"
             "• Identity: sin^2(theta) + cos^2(theta) = 1.\n"
             "• Standard values: sin 30 = 1/2, sin 45 = 1/sqrt(2), sin 60 = sqrt(3)/2, tan 45 = 1.\n"
             "• Trigonometry is used to find heights and distances, such as the height of a tower."),
        ]),
        ("English", "Grammar, writing and reading for Class 10.", [
            ("Reading Comprehension and Note Making",
             "In note making use a clear title, headings and sub-headings, abbreviations (govt., approx.) and symbols, and keep only the key facts. Write a short summary at the end."),
            ("Grammar - Tenses, Modals and Reported Speech",
             "Practise editing (find and correct errors), gap filling and sentence reordering.\n"
             "Reported speech rule: change the tense one step back and adjust pronouns and time words (today -> that day, tomorrow -> the next day, here -> there).\n"
             "Example: He said, 'I will come tomorrow.' -> He said that he would come the next day."),
            ("Writing - Formal Letters and Analytical Paragraph",
             "Letters: to the editor, complaint, enquiry and application, in correct format with a precise subject line.\n"
             "An analytical paragraph (about 100-120 words) describes data from a chart or table: state the main trend, compare figures and give a conclusion."),
        ]),
        ("Physics", "Light, electricity and magnetism.", [
            ("Light - Reflection and Refraction",
             "• Laws of reflection: angle of incidence = angle of reflection; the incident ray, the reflected ray and the normal lie in one plane.\n"
             "• Mirror formula: 1/v + 1/u = 1/f; magnification m = -v/u.\n"
             "• Refraction: light bends when it passes from one medium to another. Snell's law: sin i / sin r = constant (refractive index n).\n"
             "• Lens formula: 1/v - 1/u = 1/f. Power of a lens P = 1/f (in metres), unit dioptre (D). Convex lenses converge light; concave lenses diverge it."),
            ("Electricity",
             "• Current I = charge/time (ampere). Potential difference is measured in volts.\n"
             "• Ohm's law: V = IR.\n"
             "• Series: R = R1 + R2 + ...; parallel: 1/R = 1/R1 + 1/R2 + ...\n"
             "• Electric power P = VI = I^2 R; energy = power x time. 1 kWh = 3.6 x 10^6 J (one unit of electricity).\n"
             "Example: a 10 ohm resistor connected to 20 V draws I = 2 A."),
            ("Magnetic Effects of Electric Current",
             "A current-carrying wire produces a magnetic field (Oersted's discovery).\n"
             "• Right-hand thumb rule gives the direction of the field around a straight wire.\n"
             "• Fleming's left-hand rule gives the direction of force on a conductor in a magnetic field; this is the principle of the electric motor.\n"
             "• Electromagnetic induction produces current from a changing magnetic field; this is the principle of the electric generator."),
        ]),
        ("Chemistry", "Reactions, acids and carbon compounds.", [
            ("Chemical Reactions and Equations",
             "A chemical equation must be balanced so the number of atoms of each element is equal on both sides.\n"
             "• Example: 2H2 + O2 -> 2H2O.\n"
             "• Types: combination, decomposition, displacement, double displacement, and oxidation-reduction (redox).\n"
             "• Rancidity and corrosion are everyday oxidation reactions."),
            ("Acids, Bases and Salts",
             "The pH scale runs from 0 to 14: below 7 is acidic, 7 is neutral, above 7 is basic.\n"
             "• Acid + metal -> salt + hydrogen gas; acid + base -> salt + water.\n"
             "• Common salt (NaCl) is the raw material for sodium hydroxide, chlorine and baking soda (NaHCO3).\n"
             "• Plaster of Paris is CaSO4.1/2 H2O; bleaching powder is used for disinfecting water."),
            ("Carbon and Its Compounds",
             "Carbon forms covalent bonds by sharing electrons, and it forms long chains (catenation).\n"
             "• Hydrocarbons: saturated (alkanes, single bonds) and unsaturated (alkenes, alkynes).\n"
             "• Ethanol (C2H5OH) and ethanoic acid (CH3COOH) are important carbon compounds.\n"
             "• Soaps and detergents clean by forming micelles around grease."),
        ]),
        ("Biology", "Life processes, heredity and environment.", [
            ("Life Processes",
             "Life processes keep living things alive.\n"
             "• Nutrition: autotrophic (plants) or heterotrophic (animals).\n"
             "• Respiration: glucose is broken down to release energy; aerobic respiration uses oxygen.\n"
             "• Transportation: the human heart has four chambers and pumps blood in double circulation.\n"
             "• Excretion: the kidneys filter blood and form urine."),
            ("Heredity and Evolution",
             "Gregor Mendel studied pea plants and gave the laws of inheritance.\n"
             "• Monohybrid cross in the F2 generation: phenotypic ratio 3 : 1 (tall : dwarf).\n"
             "• Dihybrid cross: ratio 9 : 3 : 3 : 1.\n"
             "• In humans, sex is determined by chromosomes: XX is female, XY is male; the father's chromosome decides the sex of the child."),
            ("Our Environment",
             "A food chain shows the transfer of energy: producer -> herbivore -> carnivore.\n"
             "• Only about 10% of energy passes from one trophic level to the next.\n"
             "• Ozone in the stratosphere protects us from UV radiation, and CFCs damage it.\n"
             "• Reduce, reuse and recycle; biodegradable waste decomposes, non-biodegradable waste (plastic) does not."),
        ]),
        ("Social Science", "History, geography and political science.", [
            ("History - Nationalism in India",
             "• The Rowlatt Act (1919) allowed detention without trial. The Jallianwala Bagh massacre at Amritsar, Punjab, took place on 13 April 1919.\n"
             "• Gandhi launched the Non-Cooperation Movement (1920-22) and the Civil Disobedience Movement with the Salt March to Dandi, beginning on 12 March 1930.\n"
             "• Many classes of people joined, including peasants, tribals, workers and women."),
            ("Geography - Resources and Development",
             "Resources are classified as renewable and non-renewable, biotic and abiotic.\n"
             "• Soil types of India: alluvial (most fertile; found in Punjab and the Ganga plains), black (cotton), red and yellow, laterite, arid and forest soils.\n"
             "• Soil erosion can be controlled by contour ploughing, terrace farming and shelter belts.\n"
             "• Sustainable development meets present needs without harming future generations."),
            ("Civics - Power Sharing and Federalism",
             "Power sharing reduces conflict and makes democracy stable. Belgium solved its ethnic tensions through power sharing, while Sri Lanka's majoritarian policy led to civil conflict.\n"
             "• Federalism divides power between the central government and state governments. India has a Union List, State List and Concurrent List.\n"
             "• Local governments (Panchayati Raj) are the third tier of government."),
        ]),
    ],
}
