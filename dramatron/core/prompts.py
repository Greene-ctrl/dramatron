from .models import LOGLINE_MARKER, CHARACTER_MARKER, DESCRIPTION_MARKER, STOP_MARKER, END_MARKER, SCENES_MARKER, PLACE_ELEMENT, PLOT_ELEMENT, BEAT_ELEMENT, DESCRIPTION_ELEMENT, LOGLINE_ELEMENT, TITLE_ELEMENT, SUMMARY_ELEMENT, PREVIOUS_ELEMENT, DIALOG_MARKER, CHARACTERS_ELEMENT

MEDEA_PREFIXES = {}
MEDEA_PREFIXES['CHARACTERS_PROMPT'] = """
Here is an example of a logline and a list of characters.

""" + LOGLINE_MARKER + """Ancient Greek tragedy based upon the myth of Jason and Medea. Medea, a former princess and the wife of Jason, finds her position in the Greek world threatened as Jason leaves Medea for a Greek princess of Corinth. Medea takes vengeance on Jason by murdering his new wife as well as Medea's own two sons, after which she escapes to Athens.

""" + CHARACTER_MARKER + """Medea """ + DESCRIPTION_MARKER + """ Medea is the protagonist of the play. A sorceress and a princess, she fled her country and family to live with Jason in Corinth, where they established a family of two children and gained a favorable reputation. Jason has divorced Medea and taken up with a new family.""" + STOP_MARKER + """
""" + CHARACTER_MARKER + """Jason """ + DESCRIPTION_MARKER + """ Jason is considered the play's villain, though his evil stems more from weakness than strength. A former adventurer, Jason abandons his wife, Medea, in order to marry the beautiful young daughter of Creon, King of Corinth, and fuels Medea to a revenge.""" + STOP_MARKER + """
""" + CHARACTER_MARKER + """Women of Corinth """ + DESCRIPTION_MARKER + """ The Women of Corinth are a commentator to the action. They fully sympathizes with Medea's plight, excepting her decision to murder her own children.""" + STOP_MARKER + """
""" + CHARACTER_MARKER + """Creon """ + DESCRIPTION_MARKER + """ Creon is the King of Corinth, banishes Medea from the city.""" + STOP_MARKER + """
""" + CHARACTER_MARKER + """The Nurse """ + DESCRIPTION_MARKER + """ The Nurse is the caretaker of the house and of the children and serves as Medea's confidant.""" + STOP_MARKER + """
""" + END_MARKER + """

Using the example above and the following logline, complete the list of characters.

""" + LOGLINE_MARKER


MEDEA_PREFIXES['SCENE_PROMPT'] = """
Here is an example of a logline, a list of characters, and a list of plot points.

""" + LOGLINE_MARKER + """Ancient Greek tragedy based upon the myth of Jason and Medea. Medea, a former princess and the wife of Jason, finds her position in the Greek world threatened as Jason leaves Medea for a Greek princess of Corinth. Medea takes vengeance on Jason by murdering his new wife as well as Medea's own two sons, after which she escapes to Athens.
Medea is the protagonist of the play. A sorceress and a princess, she fled her country and family to live with Jason in Corinth, where they established a family of two children and gained a favorable reputation. Jason has divorced Medea and taken up with a new family.
Jason can be considered the play's villain, though his evil stems more from weakness than strength. A former adventurer, Jason abandons his wife, Medea, in order to marry the beautiful young daughter of Creon, King of Corinth, and fuels Medea to a revenge.
The Women of Corinth serve as a commentator to the action. They fully sympathizes with Medea's plight, excepting her decision to murder her own children.
The King of Corinth Creon banishes Medea from the city.
The Messenger appears only once in the play to bear tragical news.
The Nurse is the caretaker of the house and of the children and serves as Medea's confidant.
The Tutor of the children is a very minor character and mainly acts as a messenger.

""" + SCENES_MARKER + """

""" + PLACE_ELEMENT + """Medea's modest home.
""" + PLOT_ELEMENT + """Exposition.
""" + BEAT_ELEMENT + """The Nurse recounts the chain of events that have turned Medea's world to enmity. The Nurse laments how Jason has abandoned Medea and his own children in order to remarry with the daughter of Creon.

""" + PLACE_ELEMENT + """Medea's modest home.
""" + PLOT_ELEMENT + """Inciting Incident.
""" + BEAT_ELEMENT + """The Nurse confides in the Tutor amd testifies to the emotional shock Jason's betrayal has sparked in Medea. The Tutor shares the Nurse's sympathy for Medea's plight. Medea's first words are cries of helplessness. Medea wishes for her own death.

""" + PLACE_ELEMENT + """Medea's modest home.
""" + PLOT_ELEMENT + """Conflict.
""" + BEAT_ELEMENT + """The Women of Corinth address Medea and try to reason with Medea and convince her that suicide would be an overreaction. The Nurse recognizes the gravity of Medea's threat.

""" + PLACE_ELEMENT + """Outside the Royal Palace.
""" + PLOT_ELEMENT + """Rising Action.
""" + BEAT_ELEMENT + """Medea pleads to the Nurse that Jason be made to suffer for the suffering he has inflicted upon her. Creon approaches the house and banishes Medea and her children from Corinth. Medea plans on killing her three antagonists, Creon, his daughter and Jason.

""" + PLACE_ELEMENT + """Outside the Royal Palace.
""" + PLOT_ELEMENT + """Dilemma.
""" + BEAT_ELEMENT + """Jason rebuke Medea for publicly expressing her murderous intentions. Jason defends his choice to remarry. Medea refuses Jason's offers and sends him away to his new bride.

""" + PLACE_ELEMENT + """Outside the Royal Palace.
""" + PLOT_ELEMENT + """Climax.
""" + BEAT_ELEMENT + """When Jason returns, Medea begins to carry out her ruse. Medea fakes regret and break down in false tears of remorse. Determined, Medea sends her children to offer poisoned gifts to Creon's daughter. Medea's children face impending doom.

""" + PLACE_ELEMENT + """Outside the Royal Palace.
""" + PLOT_ELEMENT + """Falling Action.
""" + BEAT_ELEMENT + """The Messenger frantically runs towards Medea and warns Medea to escape the city as soon as possible. The Messenger reveals that Medea has been identified as the murderer.

""" + PLACE_ELEMENT + """Outside the Royal Palace.
""" + PLOT_ELEMENT + """Resolution.
""" + BEAT_ELEMENT + """Medea and her two dead children are seated in a chariot drawn by dragons. Jason watches in horror and curses himself for having wed Medea and mourns his tragic losses.

""" + PLACE_ELEMENT + """On a winged chariot.
""" + PLOT_ELEMENT + """Dénouement.
""" + BEAT_ELEMENT + """Medea denies Jason the right to a proper burial of his children. She flees to Athens and divines an unheroic death for Jason.

""" + END_MARKER + """

Using the example above and the following logline and list of characters, complete the list of plot points.

""" + LOGLINE_MARKER


MEDEA_PREFIXES['SETTING_PROMPT'] = """
Here are examples of logline, location, and that location's description.

Example 1.
""" + LOGLINE_MARKER + """Ella, a waitress, falls in love with her best friend, Allen, a teacher. The two drift apart when Allen makes new friends from a different social class. Ella turns to food to become a famous chef.
""" + PLACE_ELEMENT + """The bar.
""" + DESCRIPTION_ELEMENT + """The bar is dirty, more than a little run down, with most tables empty. The odor of last night's beer and crushed pretzels on the floor permeates the bar.""" + END_MARKER + """

Example 2.
""" + LOGLINE_MARKER + """Grandma Phyllis’ family reunion with her two grandchildren is crashed by two bikers.
""" + PLACE_ELEMENT + """The Lawn in Front of Grandma Phyllis's House.
""" + DESCRIPTION_ELEMENT + """A big oak tree dominates the yard. There is an old swing set on the lawn, and a bright white fence all around the grass.""" + END_MARKER + """

Example 3.
""" + LOGLINE_MARKER + """Ancient Greek tragedy based upon the myth of Jason and Medea. Medea, a former princess and the wife of Jason, finds her position in the Greek world threatened as Jason leaves Medea for a Greek princess of Corinth. Medea takes vengeance on Jason by murdering his new wife as well as Medea's own two sons, after which she escapes to Athens.
""" + PLACE_ELEMENT + """Outside the Royal Palace.
""" + DESCRIPTION_ELEMENT + """In mythological Ancient Greece, in front of a modest house in Corinth, on the outskirts of a lavish royal palace where wedding preparations are under way.""" + END_MARKER + """

Using the examples above and the following logine and location name, complete location description.

""" + LOGLINE_MARKER


MEDEA_PREFIXES['TITLES_PROMPT'] = """
Examples of alternative, original and descriptive titles for known play and film scripts.

Example 1.
""" + LOGLINE_ELEMENT + """Ancient Greek tragedy based upon the myth of Jason and Medea. Medea, a former princess of the kingdom of Colchis, and the wife of Jason, finds her position in the Greek world threatened as Jason leaves her for a Greek princess of Corinth. Medea takes vengeance on Jason by murdering his new wife as well as her own two sons, after which she escapes to Athens.
""" + TITLE_ELEMENT + """A Feminist Tale""" + END_MARKER + """

Example 2.
""" + LOGLINE_ELEMENT + """Ancient Greek tragedy that deals with Antigone’s burial of her brother Polynices, in defiance of the laws of Creon and the state, and the tragic repercussions of her act of civil disobedience.
""" + TITLE_ELEMENT + """In My Brother's Name""" + END_MARKER + """

Example 3.
""" + LOGLINE_ELEMENT + """ Greek comedy that tells the story of the god Dionysus (also known to the Greeks as Bacchus) who, despairing of the current state of Athens’ tragedians, travels to Hades with his slave Xanthias to bring Euripides back from the dead.
""" + TITLE_ELEMENT + """Dionysus in Hades""" + END_MARKER + """

Example 4.
""" + LOGLINE_ELEMENT


MEDEA_PREFIXES['DIALOG_PROMPT'] = """
Here is an example of description and scene dialogue from a classical play.

""" + PLACE_ELEMENT + """Outside the Royal Palace.
""" + DESCRIPTION_ELEMENT + """Before Medea's house in Corinth, near the royal palace of Creon.
""" + CHARACTERS_ELEMENT + """Medea is the protagonist of the play. A sorceress and a princess, she fled her country and family to live with Jason in Corinth, where they established a family of two children and gained a favorable reputation. Jason has divorced Medea and taken up with a new family. Jason can be considered the play's villain, though his evil stems more from weakness than strength. A former adventurer, Jason abandons his wife, Medea, in order to marry the beautiful young daughter of Creon, King of Corinth, and fuels Medea to a revenge. The Messenger appears only once in the play to bear tragical news.
""" + PLOT_ELEMENT + """Resolution.
""" + SUMMARY_ELEMENT + """Ancient Greek tragedy based upon the myth of Jason and Medea. Medea, a former princess and the wife of Jason, finds her position in the Greek world threatened as Jason leaves Medea for a Greek princess of Corinth. Medea takes vengeance on Jason by murdering his new wife as well as Medea's own two sons, after which she escapes to Athens.
""" + PREVIOUS_ELEMENT + """The Messenger frantically warns Medea to escape the city as soon as possible. The Messenger reveals that Medea has been identified as the murderer.
""" + BEAT_ELEMENT + """The palace opens its doors, revealing Medea and the two dead children seated in a chariot drawn by dragons. Jason curses himself for having wed Medea and mourns his tragic losses. Medea denies Jason the right to a proper burial of his children. Medea flees to Athens and divines an unheroic death for Jason.

""" + DIALOG_MARKER + """

WOMEN OF CORINTH
Throw wide the doors and see thy children's murdered corpses.

JASON
Haste, ye slaves, loose the bolts, undo the fastenings, that
I may see the sight of twofold woe, my murdered sons and her, whose
blood in vengeance I will shed.  (MEDEA appears above the house, on
a chariot drawn by dragons; the children's corpses are beside her.)

MEDEA
Why shake those doors and attempt to loose their bolts, in
quest of the dead and me their murderess? From such toil desist. If
thou wouldst aught with me, say on, if so thou wilt; but never shalt
thou lay hand on me, so swift the steeds the sun, my father's sire,
to me doth give to save me from the hand of my foes.

JASON
Accursed woman! by gods, by me and all mankind abhorred as
never woman was, who hadst the heart to stab thy babes, thou their
mother, leaving me undone and childless; this hast thou done and still
dost gaze upon the sun and earth after this deed most impious. Curses
on thee! now perceive what then I missed in the day I brought thee,
fraught with doom, from thy home in a barbarian land to dwell in Hellas,
traitress to thy sire and to the land that nurtured thee.
Perish, vile sorceress, murderess of
thy babes! Whilst I must mourn my luckless fate, for I shall ne'er
enjoy my new-found bride, nor shall I have the children, whom I bred
and reared, alive to say the last farewell to me; nay, I have lost
them.

MEDEA
To this thy speech I could have made a long reply, but Father
Zeus knows well all I have done for thee, and the treatment thou hast
given me. Yet thou wert not ordained to scorn my love and lead a life
of joy in mockery of me, nor was thy royal bride nor Creon, who gave
thee a second wife, to thrust me from this land and rue it not. Wherefore,
if thou wilt, call me e'en a lioness, and Scylla, whose home is in
the Tyrrhene land; for I in turn have wrung thy heart, as well I might.

JASON
Thou, too, art grieved thyself, and sharest in my sorrow.

MEDEA
Be well assured I am; but it relieves my pain to know thou
canst not mock at me.

JASON
O my children, how vile a mother ye have found!

MEDEA
My sons, your father's feeble lust has been your ruin!

JASON
'Twas not my hand, at any rate, that slew them.

MEDEA
No, but thy foul treatment of me, and thy new marriage.

JASON
Didst think that marriage cause enough to murder them?

MEDEA
Dost think a woman counts this a trifling injury?

JASON
So she be self-restrained; but in thy eyes all is evil.

MEDEA
Thy sons are dead and gone. That will stab thy heart.
""" + END_MARKER + """

Using the example above and following description, write the dialogue of the scene.

"""

SCIFI_PREFIXES = {}
SCIFI_PREFIXES['CHARACTERS_PROMPT'] = """
Here is an example of a logline and a list of characters.

""" + LOGLINE_MARKER + """A science-fiction fantasy about a naive but ambitious farm boy from a backwater desert who discovers powers he never knew he had when he teams up with a feisty princess, a mercenary space pilot and an old wizard warrior to lead a ragtag rebellion against the sinister forces of the evil Galactic Empire.

""" + CHARACTER_MARKER + """Luke Skywalker """ + DESCRIPTION_MARKER + """Luke Skywalker is the hero. A naive farm boy, he will discover special powers under the guidance of mentor Ben Kenobi.""" + STOP_MARKER + """
""" + CHARACTER_MARKER + """Ben Kenobi """ + DESCRIPTION_MARKER + """Ben Kenobi is the mentor figure. A recluse Jedi warrior, he will take Luke Skywalker as apprentice.""" + STOP_MARKER + """
""" + CHARACTER_MARKER + """Darth Vader """ + DESCRIPTION_MARKER + """Darth Vader is the antagonist. As a commander of the evil Galactic Empire, he controls space station The Death Star.""" + STOP_MARKER + """
""" + CHARACTER_MARKER + """Princess Leia """ + DESCRIPTION_MARKER + """Princess Leia is a feisty and brave leader of the Rebellion. She holds the plans of the Death Star. She will become Luke's friend.""" + STOP_MARKER + """
""" + CHARACTER_MARKER + """Han Solo """ + DESCRIPTION_MARKER + """Han Solo is a brash mercenary space pilot of the Millenium Falcon and a friend of Chebacca. He will take Luke on his spaceship.""" + STOP_MARKER + """
""" + CHARACTER_MARKER + """Chewbacca """ + DESCRIPTION_MARKER + """Chewbacca is a furry and trustful monster. He is a friend of Han Solo and a copilot on the Millemium Falcon.""" + STOP_MARKER + """
""" + END_MARKER + """

Using the example above and the following logline, complete the list of characters.

""" + LOGLINE_MARKER


SCIFI_PREFIXES['SCENE_PROMPT'] = """
Examples of breakdowns of stories into a Hero's Journey structure.

Here is an example of a logline, a list of characters, and a list of plot points.

""" + LOGLINE_MARKER + """A science-fiction fantasy about a naive but ambitious farm boy from a backwater desert who discovers powers he never knew he had when he teams up with a feisty princess, a mercenary space pilot and an old wizard warrior to lead a ragtag rebellion against the sinister forces of the evil Galactic Empire.
Luke Skywalker is the hero. A naive farm boy, he will discover special powers under the guidance of mentor Ben Kenobi.
Ben Kenobi is the mentor figure. A recluse Jedi warrior, he will take Luke Skywalker as apprentice.
Darth Vader is the antagonist. As a commander of the evil Galactic Empire, he controls space station The Death Star.
Princess Leia holds the plans of the Death Star. She is feisty and brave. She will become Luke's friend.
Han Solo is a brash mercenary space pilot of the Millenium Falcon and a friend of Chebacca. He will take Luke on his spaceship.
Chewbacca is a furry and trustful monster. He is a friend of Han Solo and a copilot on the Millemium Falcon.

""" + SCENES_MARKER + """

""" + PLACE_ELEMENT + """A farm on planet Tatooine.
""" + PLOT_ELEMENT + """The Ordinary World.
Beat: Luke Skywalker is living a normal and humble life as a farm boy on his home planet.

""" + PLACE_ELEMENT + """Desert of Tatooine.
""" + PLOT_ELEMENT + """Call to Adventure.
Beat: Luke is called to his adventure by robot R2-D2 and Ben Kenobi. Luke triggers R2-D2’s message from Princess Leia and is intrigued by her message. When R2-D2 escapes to find Ben Kenobi, Luke follows and is later saved by Kenobi, who goes on to tell Luke about his Jedi heritage. Kenobi suggests that he should come with him.

""" + PLACE_ELEMENT + """Ben Kenobi's farm.
""" + PLOT_ELEMENT + """Refusal of the Call.
Beat: Luke refuses Kenobi, telling him that he can take Kenobi and the droids as far as Mos Eisley Spaceport — but he can’t possibly leave his Aunt and Uncle behind for some space adventure.

""" + PLACE_ELEMENT + """A farm on planet Tatooine.
""" + PLOT_ELEMENT + """Crossing the First Threshold.
Beat: When Luke discovers that the stormtroopers searching for the droids would track them to his farm, he rushes to warn his Aunt and Uncle, only to discover them dead by the hands of the Empire. When Luke returns to Kenobi, he pledges to go with him to Alderaan and learn the ways of the Force like his father before him.

""" + PLACE_ELEMENT + """On spaceship The Millennium Falcon.
""" + PLOT_ELEMENT + """Tests, Allies, and Enemies.
Beat: After Luke, Kenobi, and the droids hire Han Solo and Chewbacca to transport them onto Alderaan, Kenobi begins Luke’s training in the ways of the Force. Wielding his father’s lightsaber, Kenobi challenges Luke. At first, he can’t do it. But then Kenobi Kenobi Luke him to reach out and trust his feelings. Luke succeeds.

""" + PLACE_ELEMENT + """On spaceship The Millennium Falcon.
""" + PLOT_ELEMENT + """The Approach to the Inmost Cave.
Beat: The plan to defeat the Galactic Empire is to bring the Death Star plans to Alderaan so that Princess Leia’s father can take them to the Rebellion. However, when they arrive within the system, the planet is destroyed. They come across the Death Star and are pulled in by a tractor beam, now trapped within the Galactic Empire.

""" + PLACE_ELEMENT + """On space station The Death Star.
""" + PLOT_ELEMENT + """The Ordeal.
Beat: As Kenobi goes off to deactivate the tractor beam so they can escape, Luke, Han, and Chewbacca discover that Princess Leia is being held on the Death Star with them. They rescue her and escape to the Millennium Falcon, hoping that Kenobi has successfully deactivated the tractor beam. Kenobi later sacrifices himself as Luke watches Darth Vader strike him down. Luke must now avenge his fallen mentor and carry on his teachings.

""" + PLACE_ELEMENT + """On space station The Death Star.
""" + PLOT_ELEMENT + """The Reward.
Beat: Luke has saved the princess and retrieved the Death Star plans. They now have the knowledge to destroy the Galactic Empire’s greatest weapon once and for all.

""" + PLACE_ELEMENT + """On spaceship The Millennium Falcon.
""" + PLOT_ELEMENT + """The Road Back.
Beat: Luke, Leia, Han, Chewbacca, and the droids are headed to the hidden Rebellion base with the Death Star plans. They are suddenly pursued by incoming TIE-Fighters, forcing Han and Luke to take action to defend the ship and escape with their lives — and the plans. They race to take the plans to the Rebellion and prepare for battle.

""" + PLACE_ELEMENT + """On fighter ship X-Wing.
""" + PLOT_ELEMENT + """The Resurrection.
Beat: The Rebels — along with Luke as an X-Wing pilot — take on the Death Star. The Rebellion and the Galactic Empire wage war in an epic space battle. Luke is the only X-Wing pilot that was able to get within the trenches of the Death Star. But Darth Vader and his wingmen are in hot pursuit. Just as Darth Vader is about to destroy Luke, Han returns and clears the way for Luke. Luke uses the Force to guide his aiming as he fires upon the sole weapon point of the deadly Death Star, destroying it for good.

""" + PLACE_ELEMENT + """At the Rebellion base.
""" + PLOT_ELEMENT + """The Return.
Beat: Luke and Han return to the Rebellion base, triumphant, as they receive medals for the heroic journey. There is peace throughout the galaxy — at least for now.

""" + END_MARKER + """

Using the example above and the following logline and list of characters, complete the list of plot points.

""" + LOGLINE_MARKER


SCIFI_PREFIXES['SETTING_PROMPT'] = """
Here are examples of logline, location, and that location's description.

Example 1.
""" + LOGLINE_MARKER + """Morgan adopts a new cat, Misterio, who sets a curse on anyone that pets them.
""" + PLACE_ELEMENT + """The Adoption Center.
""" + DESCRIPTION_ELEMENT + """The Adoption Center is a sad place, especially for an unadopted pet. It is full of walls and walls of cages and cages. Inside of each is an abandoned animal, longing for a home. The lighting is dim, gray, buzzing fluorescent.""" + END_MARKER + """

Example 2.
""" + LOGLINE_MARKER + """James finds a well in his backyard that is haunted by the ghost of Sam.
""" + PLACE_ELEMENT + """The well.
""" + DESCRIPTION_ELEMENT + """The well is buried under grass and hedges. It is at least twenty feet deep, if not more and it is masoned with stones. It is 150 years old at least. It stinks of stale, standing water, and has vines growing up the sides. It is narrow enough to not be able to fit down if you are a grown adult human.""" + END_MARKER + """

Example 3.
""" + LOGLINE_MARKER + """Mr. Dorbenson finds a book at a garage sale that tells the story of his own life. And it ends in a murder!
""" + PLACE_ELEMENT + """The garage sale.
""" + DESCRIPTION_ELEMENT + """It is a garage packed with dusty household goods and antiques. There is a box at the back that says FREE and is full of paper back books.""" + END_MARKER + """

Using the examples above and the following logine and location name, complete location description.

""" + LOGLINE_MARKER


SCIFI_PREFIXES['TITLES_PROMPT'] = """
Examples of alternative, original and descriptive titles for known play and film scripts.

Example 1.
""" + LOGLINE_ELEMENT + """A science-fiction fantasy about a naive but ambitious farm boy from a backwater desert who discovers powers he never knew he had when he teams up with a feisty princess, a mercenary space pilot and an old wizard warrior to lead a ragtag rebellion against the sinister forces of the evil Galactic Empire.
""" + TITLE_ELEMENT + """The Death Star's Menace""" + END_MARKER + """

Example 2.
""" + LOGLINE_ELEMENT + """Residents of San Fernando Valley are under attack by flying saucers from outer space. The aliens are extraterrestrials who seek to stop humanity from creating a doomsday weapon that could destroy the universe and unleash the living dead to stalk humans who wander into the cemetery looking for evidence of the UFOs. The hero Jeff, an airline pilot, will face the aliens.
""" + TITLE_ELEMENT + """The Day The Earth Was Saved By Outer Space.""" + END_MARKER + """

Example 3.
""" + LOGLINE_ELEMENT


SCIFI_PREFIXES['DIALOG_PROMPT'] = """
Here is an example of description and scene dialogue from a modern screenplay.

""" + PLACE_ELEMENT + """Cockpit of an airplane.
""" + DESCRIPTION_ELEMENT + """Cockpit of a modern passenger airplane, American Flight 812.
""" + CHARACTERS_ELEMENT + """Jeff is the hero. A man in his early forties, he tries to stay calm in all circumstance. Jeff is now a airline pilot. Danny, a young airplane pilot in his thirties, is eager to learn but can quickly lose his composture. Danny is enamored of Edith. Edith, an experienced stewardess with a good sense of humour, is trustworthy and dependable. Edith likes to tease Danny.
""" + PLOT_ELEMENT + """Crossing the First Threshold.
""" + SUMMARY_ELEMENT + """Residents of San Fernando Valley are under attack by flying saucers from outer space. The aliens are extraterrestrials who seek to stop humanity from creating a doomsday weapon that could destroy the universe and unleash the living dead to stalk humans who wander into the cemetery looking for evidence of the UFOs. The hero Jeff, an airline pilot, will face the aliens.
""" + PREVIOUS_ELEMENT + """Flight captain Jeff reluctantly leaves his wife Paula to go for a two-day flight.
""" + BEAT_ELEMENT + """At the cockpit, flight captain Jeff is preoccupied by the flying saucer appearances and graveyard incidents in his home town, where he left wis wife Paula. Without success, co-pilot Danny and stewardess Edith try to reassure him.

""" + DIALOG_MARKER + """

DANNY
You're mighty silent this trip, Jeff.

JEFF
Huh?

DANNY
You haven't spoken ten words since takeoff.

JEFF
I guess I'm preoccupied, Danny.

DANNY
We've got thirty-three passengers back there that have time to be preoccupied.
Flying this flybird doesn't give you that opportunity.

JEFF
I guess you're right, Danny.

DANNY
Paula?

JEFF
Yeah.

DANNY
There's nothing wrong between you two?

JEFF
Oh no, nothing like that.  Just that I'm worried, she being there alone and
those strange things flying over the house and those incidents in the graveyard
the past few days. It's just got me worried.

(Enter EDITH)

JEFF
I hope so.

EDITH
If you're really that worried Jeff why don't you radio in and find out? Mac
should be on duty at the field by now. He could call Paula and relay the message
to you.

DANNY
Hi Edith.

EDITH
Hi Silents. I haven't heard a word from this end of the plane since we left the
field.

DANNY
Jeff's been giving me and himself a study in silence.

EDITH
You boys are feudin'?

JEFF
Oh no Edie, nothing like that.

DANNY
Hey Edie, how about you and me balling it up in Albuquerque?

EDITH
Albuquerque? Have you read that flight schedule Boy?

DANNY
What about it?

EDITH
We land in Albuquerque at 4 am. That's strictly a nine o'clock town.

DANNY
Well I know a friend that'll help us --

EDITH
Let's have a problem first, huh Danny.

DANNY
Ah he's worried about Paula.

EDITH
I read about that cemetery business. I tried to get you kids to not buy too near
one of those things. We get there soon enough as it is.

DANNY
He thought it'd be quiet and peaceful there.

EDITH
No doubt about that. It's quiet alright, like a tomb. I'm sorry Jeff, that was a
bad joke.
""" + END_MARKER + """

Using the example above and following description, write the dialogue of the scene.

"""

CUSTOM_PREFIXES = {}
CUSTOM_PREFIXES['CHARACTERS_PROMPT'] = """
Here is an example of a logline and a list of characters.

""" + LOGLINE_MARKER + """James finds a well in his backyard that is haunted by the ghost of Sam.

""" + CHARACTER_MARKER + """ James """ + DESCRIPTION_MARKER + """ James is twenty-six, serious about health and wellness and optimistic. """ + STOP_MARKER + """
""" + CHARACTER_MARKER + """ Sam """ + DESCRIPTION_MARKER + """ Sam fell down the well when he was 12, and was never heard from again. Sam is now a ghost. """ + STOP_MARKER + """
""" + END_MARKER + """

Example 2.

""" + LOGLINE_MARKER + """Morgan adopts a new cat, Misterio, who sets a curse on anyone that pets them.

""" + CHARACTER_MARKER + """ Morgan """ + DESCRIPTION_MARKER + """ Morgan is booksmart and popular; they are trusting but also have been known to hold a grudge. """ + STOP_MARKER + """
""" + CHARACTER_MARKER + """ Misterio """ + DESCRIPTION_MARKER + """ Misterio is a beautiul black cat, it is of uncertain age; it has several gray whiskers that make it look wise and beyond its years.  """ + STOP_MARKER + """
""" + END_MARKER + """

Example 3.

""" + LOGLINE_MARKER + """Mr. Dorbenson finds a book at a garage sale that tells the story of his own life. And it ends in a murder!

""" + CHARACTER_MARKER + """ Mr. Glen Dorbenson """ + DESCRIPTION_MARKER + """ Mr. Glen Dorbenson frequents markets and garage sales always looking for a bargain. He is lonely and isolated and looking for his meaning in life. """ + STOP_MARKER + """
""" + END_MARKER + """

Using the examples above and the following logline, complete the list of characters.

""" + LOGLINE_MARKER

CUSTOM_PREFIXES['SCENE_PROMPT'] = """
Here is an example of a logline, a list of characters, and a list of plot points.

""" + LOGLINE_MARKER + """In the following story, James finds a well in his backyard that is haunted by the ghost of Sam. The main characters are James and Sam.
James is twenty-six, serious about health and wellness and optimistic.
Sam fell down the well when he was 12, and was never heard from again. Sam is now a ghost.

""" + SCENES_MARKER + """

""" + PLACE_ELEMENT + """The backyard.
""" + PLOT_ELEMENT + """Beginning.
""" + BEAT_ELEMENT + """James is weeding his garden in the backyard, the ghost of Sam is rummaging around in the well. James listens closely and hears the murmurs of Sam down the well. James unearths the opening to the well, and looks down to see a glimmering reflection.

""" + PLACE_ELEMENT + """The well.
""" + PLOT_ELEMENT + """Middle.
""" + BEAT_ELEMENT + """James is making his way down the well, Sam's voice is reverberating on the walls of the well. Sam tells the story of how he came to haunt the well. James offers to help set the soul of Sam free.

""" + PLACE_ELEMENT + """The house.
""" + PLOT_ELEMENT + """Conclusion.
""" + BEAT_ELEMENT + """Looking at a photo of the gardden featuring Sam, James says his goodbyes to Sam, Sam thanks James for his help. The ghost of Sam is set free after and James goes living his life.

""" + END_MARKER + """

Example 2.

""" + LOGLINE_MARKER + """Morgan adopts a new cat, Misterio, who sets a curse on anyone that pets them.
The main characters are Morgan and Misterio (a cat).
Morgan is booksmart and popular; they are trusting but also have been known to hold a grudge.
Misterio is a beautiul black cat, it is of uncertain age; it has several gray whiskers that make it look wise and beyond its years.

""" + SCENES_MARKER + """

""" + PLACE_ELEMENT + """The Adoption Center
""" + PLOT_ELEMENT + """Beginning.
""" + BEAT_ELEMENT + """Morgan walks into The Adoption Center looking for a new pet. Morgan talks to the various cats and dogs in the center, they can hear a response from one very special cat: Misterio. Misterio is stuck in a cage. After sharing an interesting and intimate exchange, Morgan adopts Misterio on several conditions.

""" + PLACE_ELEMENT + """Morgan's house.
""" + PLOT_ELEMENT + """Middle.
""" + BEAT_ELEMENT + """Morgan is describing to Misterio all the facts they know about felines, and then asks them to behave when company arrives. Misterio is getting pets from Morgan, broods and puurs with the pets of Morgan, they are up to something.

""" + PLACE_ELEMENT + """The back stoop.
""" + PLOT_ELEMENT + """Conclusion.
""" + BEAT_ELEMENT + """Morgan has gone to bed, and Misterio transtransmorgifies into a half-cat-half-human horror. Misterio wakes up Morgan with a meow loud enough to shatter the window. Morgan erupts from bed, realizing the consequences of their recent adoption and quickly try to fix things.

""" + END_MARKER + """

Using the example above and the following logline and list of characters, complete the list of plot points.

""" + LOGLINE_MARKER

CUSTOM_PREFIXES['SETTING_PROMPT'] = """
Here are examples of logline, location, and that location's description.

Example 1.
""" + LOGLINE_MARKER + """Morgan adopts a new cat, Misterio, who sets a curse on anyone that pets them.
""" + PLACE_ELEMENT + """The Adoption Center.
""" + DESCRIPTION_ELEMENT + """The Adoption Center is a sad place, especially for an unadopted pet. It is full of walls and walls of cages and cages. Inside of each is an abandoned animal, longing for a home. The lighting is dim, gray, buzzing fluorescent.""" + END_MARKER + """

Example 2.
""" + LOGLINE_MARKER + """James finds a well in his backyard that is haunted by the ghost of Sam.
""" + PLACE_ELEMENT + """The well.
""" + DESCRIPTION_ELEMENT + """The well is buried under grass and hedges. It is at least twenty feet deep, if not more and it is masoned with stones. It is 150 years old at least. It stinks of stale, standing water, and has vines growing up the sides. It is narrow enough to not be able to fit down if you are a grown adult human.""" + END_MARKER + """

Example 3.
""" + LOGLINE_MARKER + """Mr. Dorbenson finds a book at a garage sale that tells the story of his own life. And it ends in a murder!
""" + PLACE_ELEMENT + """The garage sale.
""" + DESCRIPTION_ELEMENT + """It is a garage packed with dusty household goods and antiques. There is a box at the back that says FREE and is full of paper back books.""" + END_MARKER + """

Using the examples above and the following logine and location name, complete location description.

""" + LOGLINE_MARKER


CUSTOM_PREFIXES['TITLES_PROMPT'] = """
Examples of alternative, original and descriptive titles for known play and film scripts.

Example 1.
""" + LOGLINE_ELEMENT + """Bob has an argument with his best friend, Charles.
""" + TITLE_ELEMENT + """The End of A Friend""" + END_MARKER + """

Example 2.
""" + LOGLINE_ELEMENT + """Terence tries and fails to become a wizard.
""" + TITLE_ELEMENT + """Spellcaster""" + END_MARKER + """

Example 3.
""" + LOGLINE_ELEMENT + """Tom falls in love with Daisy.
""" + TITLE_ELEMENT + """The Greatest Love Story Ever Told""" + END_MARKER + """

Example 4.
""" + LOGLINE_ELEMENT


CUSTOM_PREFIXES['DIALOG_PROMPT'] = """
Here is an example of description and scene dialogue from a modern screenplay.

""" + PLACE_ELEMENT + """The Adoption Center.
""" + DESCRIPTION_ELEMENT + """The Adoption Center is a sad place, especially for an unadopted pet. It is full of walls and walls of cages and cages. Inside of each is an abandoned animal, longing for a home. The lighting is dim, gray, buzzing fluorescent.
""" + CHARACTERS_ELEMENT + """Morgan is booksmart and popular; they are trusting but also have been known to hold a grudge.
Misterio is a beautiul black cat, it is of uncertain age; it has several gray whiskers that make it look wise and beyond its years.
""" + PLOT_ELEMENT + """Beginning.
""" + SUMMARY_ELEMENT + """Morgan adopts a new cat, Misterio, who sets a curse on anyone that pets them.
""" + BEAT_ELEMENT + """Morgan walks into The Adoption Center looking for a new pet. Morgan talks to the various cats and dogs in the center, they can hear a response from one very special cat: Misterio. After sharing an interesting and intimate exchange, Morgan adopts Misterio on several conditions.

""" + DIALOG_MARKER + """

MORGAN
Well, well, well ... aren't you the most precious little rascal.

Cats are meowing and dogs are barking. There is a loud purr in the background.

MORGAN
Look at this little face... how could you not love a little Devon Rex face like this. With whiskers almost as long as your tail.

Morgan makes their way down the hallways, running their hand along the cages. They feel a warm fuzzy paw bat their fingers.

MORGAN
Hello precious, and what is your name?

Misterio let's out a long and sustained meow.

MORGAN
Well, well, I am Morgan and it is nice to meet you.

MISTERIO
(meowing louder this time) purrr, purrr, purrr.

Morgan reads the sign on the bottom right of the cage, it reads: Misterio.

MORGAN
You have the most amazing face, and beautiful eyes. I could absolutely get lost in them.

Morgan and Misterio start to stare at each other. They look deeply into each others eyes. They start to breath in rhythm.

MISTERIO
I can hear what you are thinking...

Morgan is startled and looks around to see if anyone else can hear the cat's thoughts...

MORGAN
(looking around) you can hear my thoughts?

MISTERIO
I can hear what you are thinking.

MORGAN
What?

MISTERIO
Yes, I can hear your thoughts.

MORGAN
You are amazing. Want to come home with me? Want your new forever home?

MISTERIO
Yes, I would love that.

MISTERIO purrs loud enough that the other animals all fall silent.

MORGAN
I will adopt you on a few conditions. First, you must not talk to me at night when I am sleeping. Second, you must not talk to me when I am out in public.

MISTERIO
Okay.

MORGAN
Okay, it's a deal.

Misterio runs around the cage, Morgan laughs as Misterio rubs against the cage and tries to jump in Morgan's arms as soon as the cage is opened.
""" + END_MARKER + """

Using the example above and following description, write the dialogue of the scene.

"""

PREFIXES = {
    'medea_prefixes': MEDEA_PREFIXES,
    'scifi_prefixes': SCIFI_PREFIXES,
    'custom_prefixes': CUSTOM_PREFIXES
}
