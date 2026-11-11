# -*- coding: utf-8 -*-
"""All site content lives here. Edit this file, rerun build.py, redeploy."""

AMZ_TAG = "bobpeckbooks-20"
SOUNDSTRUE = "https://www.soundstrue.com/store/#5e84137f6f1e1"

# ---------------------------------------------------------------- IDEAS
IDEAS = [
{
"slug": "feeling-lost",
"title": "Feeling lost",
"tags": ["Start here", "Meaning", "Change"],
"summary": "Feeling lost is common, usually temporary, and often a sign that an old map has stopped working.",
"read": 4,
"short": [
  "Lost usually means a chapter ended before the next one started.",
  "Clarity tends to follow action, not the other way around.",
  "Shrink the question until you can answer it this week.",
],
"try": "two-minute-start",
"practices": ["values-check", "two-minute-start"],
"related": ["values", "ikigai", "body-foundation", "connection"],
"body": """
<h2>What it usually is</h2>
<p>Feeling lost is rarely a defect in you. More often it is what it feels like when the story you were living in stops fitting and the next one has not formed yet. That story might be a job, a relationship, a belief, or a version of yourself. The writer William Bridges, who studied life transitions, described the stretch between an ending and a new beginning as a neutral zone. It is uncomfortable, and it is also where a lot of the real sorting-out happens.</p>
<h2>Why waiting for clarity does not work</h2>
<p>Most of us expect certainty to arrive first and action to follow. The research on career change points the other way. Herminia Ibarra, who studied people reinventing their working lives, found that they rarely planned their way into a new direction. They tried small experiments, met different people, and noticed what gave them energy. Clarity came after the trying.</p>
<h2>Make the question smaller</h2>
<p>"What is my purpose?" is too big to answer from a couch. Smaller questions can be answered this week. What is one thing I could try that I have not tried? What did I enjoy before I started judging it? Who do I admire that I could ask one question? The Japanese idea of {idea:ikigai|ikigai} is a good guide here. It treats small, everyday reasons as the real thing.</p>
<h2>Three small moves</h2>
<ol>
<li><strong>Steady the basics.</strong> Sleep, food, movement, and one real conversation. They will not fix everything, but a tired and isolated mind gets lost faster. See {idea:body-foundation}.</li>
<li><strong>Name what ended.</strong> Write one honest sentence about what you lost or outgrew. Unnamed endings tend to linger as vague dread.</li>
<li><strong>Run one experiment.</strong> A class, a walk somewhere new, an email to someone whose work interests you. Small, cheap, reversible. The {practice:two-minute-start|two-minute start} practice is built for this.</li>
</ol>
<h2>When it is more than lost</h2>
<p>If the feeling has turned into hopelessness, if nothing has interested you for weeks, or if you have thoughts of not wanting to be alive, please do not wait it out alone. Reaching out to a doctor, a therapist, or a crisis line is a strong move, not a weak one. The <a href="/help/">help page</a> lists places to start.</p>
""",
"sources": [
  "William Bridges, Transitions: Making Sense of Life's Changes (1980).",
  "Herminia Ibarra, Working Identity: Unconventional Strategies for Reinventing Your Career (2003).",
],
},
{
"slug": "discipline",
"title": "What discipline actually is",
"tags": ["Discipline", "Habits", "Start here"],
"summary": "Discipline is less about gritting your teeth and more about arranging your days so the right thing is easier.",
"read": 4,
"short": [
  "The 'willpower battery' idea has not held up well in replication.",
  "People with strong self-control tend to face fewer temptations, not resist more.",
  "Design the environment first, then rely on effort for what is left.",
],
"try": "if-then-plan",
"practices": ["if-then-plan", "two-minute-start"],
"related": ["habits", "values", "self-compassion"],
"body": """
<h2>Two meanings of the word</h2>
<p>Many people hear "discipline" and picture clenched teeth. There is an older meaning: a discipline is a practice, something you return to. The second meaning is the more useful one, because it does not depend on feeling strong today.</p>
<h2>The willpower battery problem</h2>
<p>For years a popular idea held that self-control is a limited fuel that drains with use. A large preregistered replication in 2016, run across many laboratories, found the effect to be close to zero. That does not mean effort is easy. It means the neat battery metaphor is a shaky foundation for a life.</p>
<h2>What disciplined people seem to do</h2>
<p>Marc Galla and Angela Duckworth found in 2015 that people high in self-control reported fewer temptations and leaned more on helpful habits. They were not winning more battles. They were arranging life so fewer battles showed up.</p>
<h2>Practical translation</h2>
<ul>
<li>Remove friction from what you want. Put the shoes by the door, the book on the pillow, the document already open.</li>
<li>Add friction to what you do not want. Phone in another room, app logged out, no snacks you will regret in the house.</li>
<li>Decide in advance. {idea:if-then|An if-then plan} turns a vague intention into a trigger.</li>
<li>Start absurdly small, then let it grow. See {practice:two-minute-start}.</li>
<li>Expect misses, and plan the restart. {idea:self-compassion} is part of discipline, not its opposite.</li>
</ul>
<h2>Discipline in service of what?</h2>
<p>Without a direction, discipline slides into self-punishment. Before tightening the routine, it helps to know what it is for. {idea:values} is a good place to look.</p>
""",
"sources": [
  "Hagger et al., 'A multilab preregistered replication of the ego-depletion effect,' Perspectives on Psychological Science (2016).",
  "Galla and Duckworth, 'More than resisting temptation: Beneficial habits mediate the relationship between self-control and positive life outcomes,' Journal of Personality and Social Psychology (2015).",
],
},
{
"slug": "habits",
"title": "How habits form",
"tags": ["Habits", "Discipline"],
"summary": "Habits are behaviors triggered by context, which is why changing the context works better than scolding yourself.",
"read": 4,
"short": [
  "Much daily behavior runs on cues in your surroundings, not on decisions.",
  "In one study, forming a new habit took a median of about two months, with wide variation.",
  "Replace an old routine rather than trying to delete it.",
],
"try": "two-minute-start",
"practices": ["two-minute-start", "if-then-plan"],
"related": ["discipline", "urges", "if-then"],
"body": """
<h2>Context does most of the work</h2>
<p>Psychologists Wendy Wood and David Neal argue that habits are triggered by cues in the environment, such as a place, a time, a preceding action, or a person. Once a habit is established, the cue starts the behavior with little deliberate thought. In a diary study, Wood and colleagues found that a large share of everyday actions, roughly four in ten, were repeated in the same place most days.</p>
<h2>How long does it take?</h2>
<p>You may have heard "21 days." The best-known study on the question, by Phillippa Lally and colleagues at University College London, followed 96 people building a simple new habit. The median time to reach automaticity was 66 days, and individuals ranged from 18 to 254. Missing a single day did not noticeably derail the process.</p>
<h2>Cue, routine, reward</h2>
<p>A popular way to picture a habit is a loop: a cue triggers a routine, and the routine delivers a reward. It is a simplification, but a useful one. If you want to change a habit, you can work on any part of the loop.</p>
<ul>
<li><strong>Change the cue.</strong> Move the trigger out of sight, or avoid the place where it lives.</li>
<li><strong>Keep the reward, swap the routine.</strong> If the old habit was meeting a real need (rest, company, relief), the new routine has to meet that need too.</li>
<li><strong>Attach a new habit to an existing one.</strong> "After I pour my coffee, I write one sentence."</li>
</ul>
<h2>Replace, do not erase</h2>
<p>An old habit's cues keep appearing long after you decide to quit. Plan what you will do when they do. {idea:if-then} and {idea:urges} cover how.</p>
""",
"sources": [
  "Wood and Neal, 'A new look at habits and the habit-goal interface,' Psychological Review (2007).",
  "Wood, Quinn and Kashy, 'Habits in everyday life: Thought, emotion, and action,' Journal of Personality and Social Psychology (2002).",
  "Lally et al., 'How are habits formed: Modelling habit formation in the real world,' European Journal of Social Psychology (2010).",
],
},
{
"slug": "urges",
"title": "Urges and cravings",
"tags": ["Urges", "Habits", "Mindfulness"],
"summary": "An urge is a wave. It rises, peaks, and passes, whether or not you act on it.",
"read": 4,
"short": [
  "Urges are driven by cues and states like hunger, loneliness, and fatigue.",
  "Watching an urge without acting is a learnable skill called urge surfing.",
  "If a habit is causing serious harm, add professional support.",
],
"try": "urge-surfing",
"practices": ["urge-surfing", "cyclic-sigh", "grounding-54321"],
"related": ["habits", "if-then", "connection", "self-compassion"],
"body": """
<h2>What an urge is</h2>
<p>An urge is a strong pull toward a behavior: checking your phone, having a drink, eating something you were not hungry for, lighting a cigarette, opening a site you will regret. It feels like an emergency. It is not. Urges are shaped by cues (a place, a time, a feeling) and by your state. The old recovery shorthand HALT, for hungry, angry, lonely, tired, is a rough but useful reminder that a body running low makes everything pull harder.</p>
<h2>Urge surfing</h2>
<p>The psychologist G. Alan Marlatt, a pioneer in relapse prevention, described urge surfing: instead of fighting an urge or obeying it, you watch it like a wave. It builds, crests, and falls. Many people find the sharpest part passes in minutes rather than hours, especially if they do not feed it with a story like "I cannot stand this."</p>
<h2>The steps, in short</h2>
<ol>
<li><strong>Notice and name it.</strong> "This is an urge."</li>
<li><strong>Find it in the body.</strong> Chest, stomach, hands, jaw. Describe the sensation as if to a scientist.</li>
<li><strong>Breathe slowly</strong> and keep watching. Longer exhales help. Try {practice:cyclic-sigh|the cyclic sigh}.</li>
<li><strong>Let it change.</strong> It will move, shrink, or shift.</li>
<li><strong>Do something else with your hands and feet.</strong> Walk, wash your face, call someone.</li>
</ol>
<p>The full version is in {practice:urge-surfing}.</p>
<h2>Do the environment work too</h2>
<p>Surfing is a backup. The first line of defense is making the behavior harder to reach and the alternative easier. See {idea:habits} and {idea:if-then}.</p>
<h2>A note on seriousness</h2>
<p>This page is general information, not treatment. If a habit is causing real harm to your health, relationships, or safety, or if you cannot stop despite trying, talking to a doctor, therapist, or a recovery program is a sign of good judgment. The <a href="/help/">help page</a> has places to start.</p>
""",
"sources": [
  "Marlatt and Gordon, Relapse Prevention (1985).",
  "Bowen and Marlatt, 'Surfing the urge: Brief mindfulness-based intervention for college student smokers,' Psychology of Addictive Behaviors (2009).",
],
},
{
"slug": "if-then",
"title": "If-then plans",
"tags": ["Discipline", "Habits", "Planning"],
"summary": "Deciding in advance exactly when and where you will act makes follow-through far more likely.",
"read": 3,
"short": [
  "Psychologist Peter Gollwitzer calls these implementation intentions.",
  "A meta-analysis found a medium-to-large effect on reaching goals.",
  "They work for starting things and for blocking old reflexes.",
],
"try": "if-then-plan",
"practices": ["if-then-plan"],
"related": ["habits", "discipline", "urges"],
"body": """
<h2>The idea</h2>
<p>An if-then plan links a specific cue to a specific action: <em>If it is 7:30 and I have finished my coffee, then I will write for ten minutes.</em> Peter Gollwitzer named these implementation intentions and has studied them for decades. The plan hands control to the cue, so you do not have to win an argument with yourself in the moment.</p>
<h2>Does it work?</h2>
<p>A 2006 meta-analysis by Gollwitzer and Paschal Sheeran, covering nearly a hundred studies, found a medium-to-large effect of these plans on goal attainment. As with most psychology, results vary by person and situation, but it is one of the better-supported tools around.</p>
<h2>Two kinds of plan</h2>
<ul>
<li><strong>Start plans.</strong> "If I sit down at my desk, then I open the draft before anything else."</li>
<li><strong>Block plans.</strong> "If I feel the urge to open the app, then I stand up and drink a glass of water."</li>
</ul>
<h2>Making them stick</h2>
<ul>
<li>Pick one cue that reliably happens: a time, a place, a finished task.</li>
<li>Make the action small and concrete. "Exercise" is vague. "Put on my shoes and walk to the corner" is not.</li>
<li>Write it down. Say it out loud once.</li>
<li>Limit yourself to one or two plans at a time.</li>
</ul>
<h2>What they cannot do</h2>
<p>If you do not actually want the goal, a plan will not manufacture wanting. Check the direction first with {idea:values}. The {practice:if-then-plan|if-then plan builder} exercise walks through building one.</p>
""",
"sources": [
  "Gollwitzer, 'Implementation intentions: Strong effects of simple plans,' American Psychologist (1999).",
  "Gollwitzer and Sheeran, 'Implementation intentions and goal achievement: A meta-analysis of effects and processes,' Advances in Experimental Social Psychology (2006).",
],
},
{
"slug": "values",
"title": "Values and goals",
"tags": ["Meaning", "Start here", "Planning"],
"summary": "Goals are places you can arrive. Values are directions you can keep walking. When goals collapse, values remain.",
"read": 3,
"short": [
  "A value is a direction, like 'be a good friend.' A goal is a destination, like 'text Sam today.'",
  "Values can guide you even when outcomes are out of your hands.",
  "Acceptance and Commitment Therapy builds much of its work on them.",
],
"try": "values-check",
"practices": ["values-check", "evening-review"],
"related": ["feeling-lost", "ikigai", "discipline", "stoic-control"],
"body": """
<h2>Direction versus destination</h2>
<p>Acceptance and Commitment Therapy, developed by Steven Hayes and colleagues, separates values from goals. A goal can be finished: get the job, run the race, save the money. A value cannot be finished. "Be a loving parent," "make honest work," "stay curious" are directions you keep choosing. Russ Harris compares it to heading west. You can walk west forever and never arrive.</p>
<h2>Why this matters when you feel lost</h2>
<p>People often feel lost because a goal collapsed: the job ended, the plan failed, the relationship changed. If your sense of direction was welded to that goal, everything goes dark. A value survives the loss. You may need new goals, but the compass still points somewhere.</p>
<h2>How to find yours</h2>
<p>Values are not rules and not things you ought to want. A few questions help.</p>
<ul>
<li>When did I last feel most like myself? What was I doing, and with whom?</li>
<li>What do I find myself envying in other people? Envy often points at a value.</li>
<li>If nobody could judge me, what would I spend a free Saturday on?</li>
<li>What would I want said about how I treated people?</li>
</ul>
<h2>From value to action</h2>
<p>Pick one value and ask: what is one small action this week that lives in that direction? That is a goal in service of a value, and it is the kind that lasts. The {practice:values-check|values check} exercise takes five minutes.</p>
""",
"sources": [
  "Hayes, Strosahl and Wilson, Acceptance and Commitment Therapy (1999).",
  "Russ Harris, The Happiness Trap (2008).",
],
},
{
"slug": "stoic-control",
"title": "The dichotomy of control",
"tags": ["Stoicism", "Anxiety", "Philosophy"],
"summary": "A Stoic habit of sorting everything into what is up to you and what is not, and spending your energy on the first pile.",
"read": 4,
"short": [
  "Epictetus opens his handbook by dividing the world into what is up to us and what is not.",
  "Your effort, choices, and responses are yours. Outcomes and other people's opinions are not.",
  "Modern cognitive therapy openly borrows from the Stoics.",
],
"try": "worry-sort",
"practices": ["worry-sort", "evening-review"],
"related": ["values", "self-compassion", "feeling-lost"],
"body": """
<h2>The core move</h2>
<p>Epictetus was born enslaved in the Roman world and became one of the most influential Stoic teachers. His short handbook, the Enchiridion, begins with a sorting exercise. Some things are up to us: our judgments, impulses, desires, and efforts. Some things are not: our bodies, our reputations, our wealth, and what other people do. Peace, he argues, comes from putting your effort in the first pile and releasing your grip on the second.</p>
<h2>What it looks like in practice</h2>
<p>Say you are worried about a job interview. You cannot control whether they like you. You can control how you prepare, how you show up, and how you treat yourself afterward. The worry does not vanish, but it stops being a fog and becomes a short list of things to do.</p>
<h2>Not what people think it is</h2>
<ul>
<li><strong>It is not passivity.</strong> It asks you to act fully on what is yours.</li>
<li><strong>It is not suppressing feeling.</strong> Stoics wrote at length about emotion. The aim was to examine it, not pretend it away.</li>
<li><strong>It is not a cure for injustice.</strong> Some things you cannot control still deserve a fight, and caring about them is part of a good life.</li>
</ul>
<h2>Why therapists noticed</h2>
<p>Albert Ellis and Aaron Beck, who founded rational emotive behavior therapy and cognitive therapy, both acknowledged the Stoics as an influence. The idea that our judgments about events shape our distress more than the events themselves runs through all of it.</p>
<h2>Try it</h2>
<p>The {practice:worry-sort|worry sort} exercise takes five minutes. For the source text, the Enchiridion is free in the <a href="/read/">Read</a> section.</p>
""",
"sources": [
  "Epictetus, Enchiridion (public domain translations are available free online).",
  "Donald Robertson, The Philosophy of Cognitive-Behavioural Therapy (2010).",
],
},
{
"slug": "self-compassion",
"title": "Self-compassion",
"tags": ["Self-compassion", "Discipline", "Mindfulness"],
"summary": "Treating yourself the way you would treat a struggling friend does not make you soft. It makes restarting easier.",
"read": 3,
"short": [
  "Kristin Neff describes three parts: kindness, common humanity, and mindfulness.",
  "Some studies find self-compassion increases motivation to improve after failure.",
  "Shame tends to feed the loop. Compassion tends to end it.",
],
"try": "evening-review",
"practices": ["evening-review", "body-scan"],
"related": ["discipline", "procrastination", "urges"],
"body": """
<h2>Three parts</h2>
<p>Kristin Neff, who has researched self-compassion for two decades, describes it as three things working together. <strong>Self-kindness</strong> means responding to your own pain with warmth rather than attack. <strong>Common humanity</strong> means remembering that struggle is part of being a person, not proof that you are uniquely broken. <strong>Mindfulness</strong> means noticing the pain without drowning in it or pretending it is not there.</p>
<h2>Will it make me lazy?</h2>
<p>That is the usual fear. The research suggests the opposite. In a 2012 set of experiments, Juliana Breines and Serena Chen found that people who were prompted to take a self-compassionate view of a personal failure spent more time on follow-up work than people who were not. Harsh self-criticism feels productive, but often it just adds shame, and shame tends to push people toward avoidance and relief-seeking.</p>
<h2>The restart problem</h2>
<p>Anyone who has tried to change a habit has slipped. What happens next matters more than the slip. A stream of self-attack ("I always do this") usually makes the next slip more likely. A calmer response ("That happened. What was going on right before it? What is the next small step?") keeps you in the work.</p>
<h2>A small practice</h2>
<ul>
<li>Notice the hard moment. Say quietly, "This is hard right now."</li>
<li>Remind yourself, "Other people feel this too."</li>
<li>Ask, "What would I say to a friend in this exact spot?" Then say it to yourself.</li>
</ul>
<p>The {practice:evening-review|evening review} exercise builds this in at the end of the day.</p>
""",
"sources": [
  "Kristin Neff, 'Self-compassion: An alternative conceptualization of a healthy attitude toward oneself,' Self and Identity (2003).",
  "Breines and Chen, 'Self-compassion increases self-improvement motivation,' Personality and Social Psychology Bulletin (2012).",
],
},
{
"slug": "procrastination",
"title": "Procrastination",
"tags": ["Procrastination", "Discipline", "Anxiety"],
"summary": "Procrastination is usually not laziness. It is a way of avoiding a feeling, and it works until it does not.",
"read": 3,
"short": [
  "Researchers describe it as short-term mood repair.",
  "The fix is to shrink the first step until it stops triggering the feeling.",
  "Forgiving yourself for past delay predicted less delay next time in one study.",
],
"try": "two-minute-start",
"practices": ["two-minute-start", "if-then-plan"],
"related": ["discipline", "self-compassion", "attention"],
"body": """
<h2>It is about feelings, not time</h2>
<p>Fuschia Sirois and Timothy Pychyl, who study procrastination, frame it as a mood problem. The task brings up boredom, anxiety, self-doubt, or resentment. Putting it off gives instant relief. The relief rewards the avoidance, so it repeats. Understanding this is useful because it moves the problem from "I am lazy" to "this task feels bad and I am escaping the feeling."</p>
<h2>What tends to help</h2>
<ul>
<li><strong>Make the first step tiny and physical.</strong> Not "write the report," but "open the file and type the title." See {practice:two-minute-start}.</li>
<li><strong>Time-box it.</strong> "Ten minutes, then I can stop." Often you will not.</li>
<li><strong>Name the feeling.</strong> "I feel anxious about getting this wrong." Naming takes some of the heat out.</li>
<li><strong>Lower the stakes of the first draft.</strong> Aim for bad on purpose.</li>
<li><strong>Use an {idea:if-then|if-then plan}</strong> so the starting moment is decided ahead of time.</li>
</ul>
<h2>Forgive the past</h2>
<p>In a 2010 study by Michael Wohl and colleagues, students who forgave themselves for procrastinating before a first exam procrastinated less before the next one. Beating yourself up did not help. See {idea:self-compassion}.</p>
<h2>A good talk on it</h2>
<p>Tim Urban's funny, honest TED talk on the procrastinating brain is in the <a href="/watch/">Watch</a> section.</p>
""",
"sources": [
  "Sirois and Pychyl, 'Procrastination and the priority of short-term mood regulation,' Social and Personality Psychology Compass (2013).",
  "Wohl, Pychyl and Bennett, 'I forgive myself, now I can study,' Personality and Individual Differences (2010).",
],
},
{
"slug": "attention",
"title": "Attention, dopamine, and the detox myth",
"tags": ["Attention", "Focus", "Habits"],
"summary": "Dopamine is less a pleasure chemical than a wanting chemical, and you cannot detox it. You can change what keeps pulling at you.",
"read": 4,
"short": [
  "Dopamine is tied to wanting and anticipation, not just enjoyment.",
  "'Dopamine detox' as usually described is not a real thing, but reducing cues can still help.",
  "Protect focus by changing your environment, not by trying harder.",
],
"try": "phone-free-walk",
"practices": ["phone-free-walk", "if-then-plan"],
"related": ["habits", "urges", "procrastination"],
"body": """
<h2>What dopamine actually does</h2>
<p>Dopamine is often called the pleasure chemical. Neuroscientists Kent Berridge and Terry Robinson have argued for decades that it is better understood as driving wanting, the pull toward something, more than liking, the enjoyment of it. That helps explain why you can compulsively reach for something that is not even fun anymore.</p>
<h2>The "detox" myth</h2>
<p>Internet advice sometimes says you can "detox" from dopamine by cutting stimulation. Your brain does not work that way, and you could not remove dopamine if you tried. What can help is more modest: reducing the cues and rapid-fire rewards that keep tugging at your attention, so ordinary things feel workable again.</p>
<h2>Why phones are sticky</h2>
<p>Feeds and notifications deliver unpredictable rewards, and unpredictable rewards are especially good at keeping behavior going. Researcher Gloria Mark has documented how often people switch tasks at their screens and how interrupted work costs time and adds stress. Computer scientist Cal Newport uses the term deep work for sustained, undistracted effort and argues that it is becoming both rarer and more valuable.</p>
<h2>Simple moves that help</h2>
<ul>
<li>Put the phone in another room during focus blocks. Whether its mere presence drains attention is debated, but removing it costs nothing.</li>
<li>Turn off notifications you did not ask for.</li>
<li>Work in one block of 25 to 50 minutes, one task, then a real break.</li>
<li>Practice being briefly bored. A {practice:phone-free-walk|phone-free walk} is a good start.</li>
<li>Decide ahead of time what you will do when the pull comes. See {idea:if-then}.</li>
</ul>
""",
"sources": [
  "Berridge and Robinson, 'What is the role of dopamine in reward: Hedonic impact, reward learning, or incentive salience?' Brain Research Reviews (1998).",
  "Mark, Gudith and Klocke, 'The cost of interrupted work: More speed and stress,' Proceedings of CHI (2008).",
  "Cal Newport, Deep Work (2016).",
],
},
{
"slug": "body-foundation",
"title": "The body is the foundation",
"tags": ["Sleep", "Movement", "Start here"],
"summary": "Sleep, movement, and daylight are unglamorous and they quietly decide how everything else feels.",
"read": 3,
"short": [
  "Most adults do best with seven or more hours of sleep.",
  "A large review found physical activity helps depression, anxiety, and distress.",
  "None of this replaces medical care when you need it.",
],
"try": "phone-free-walk",
"practices": ["phone-free-walk", "body-scan"],
"related": ["feeling-lost", "discipline", "connection"],
"body": """
<h2>Why start here</h2>
<p>When people feel lost, they reach for big answers: purpose, identity, a new plan. Often the body is quietly making everything harder. Little sleep, no movement, and days without daylight make worry louder and effort heavier. Fixing the basics will not solve everything, but it makes everything else more solvable.</p>
<h2>Sleep</h2>
<p>Sleep and public health organizations in the United States recommend that adults get at least seven hours a night. Some things that tend to help:</p>
<ul>
<li>A consistent wake time, even on weekends.</li>
<li>Outdoor light soon after waking.</li>
<li>Less caffeine in the afternoon and less alcohol near bedtime.</li>
<li>A dim, screen-light wind-down before bed.</li>
</ul>
<h2>Movement</h2>
<p>A 2023 overview of systematic reviews by Ben Singh and colleagues, published in the British Journal of Sports Medicine, found that physical activity interventions improved symptoms of depression, anxiety, and distress across many groups. You do not need a gym. A brisk daily walk counts, and consistency matters more than intensity.</p>
<h2>Daylight and food</h2>
<p>Getting outside in daylight helps set your body clock. Regular meals, protein, and water are boring and effective. Skipping meals and running on caffeine makes mood and cravings harder to manage.</p>
<h2>A caution</h2>
<p>This is general information, not medical advice. Ongoing sleep problems, low mood that does not lift, or anything that worries you are good reasons to talk with a doctor.</p>
""",
"sources": [
  "Centers for Disease Control and Prevention, 'About Sleep' (cdc.gov).",
  "Singh et al., 'Effectiveness of physical activity interventions for improving depression, anxiety and distress: an overview of systematic reviews,' British Journal of Sports Medicine (2023).",
],
},
{
"slug": "connection",
"title": "Connection",
"tags": ["Relationships", "Loneliness", "Meaning"],
"summary": "The quality of your relationships is one of the strongest predictors of how your life goes. Loneliness is a signal, not a verdict.",
"read": 3,
"short": [
  "The Harvard Study of Adult Development ties good relationships to health and happiness.",
  "Loneliness is a signal like hunger, pointing at a need.",
  "Small, repeated contact beats occasional big gestures.",
],
"try": "two-minute-start",
"practices": ["two-minute-start", "evening-review"],
"related": ["urges", "feeling-lost", "body-foundation"],
"body": """
<h2>What the longest study found</h2>
<p>The Harvard Study of Adult Development began in 1938 and has followed participants and their families for generations. Its current directors, Robert Waldinger and Marc Schulz, summarize a central finding: the quality of people's relationships is among the strongest predictors of health and wellbeing in later life, stronger than many things people chase instead.</p>
<h2>Loneliness as a signal</h2>
<p>Loneliness is uncomfortable the way hunger is uncomfortable. It is information that a need is unmet. People often respond by numbing it with screens, substances, or compulsive habits that work briefly and leave them lonelier. If you notice a pull toward something you would rather not do, it can help to ask whether you are actually lonely. See {idea:urges}.</p>
<h2>Small moves that work</h2>
<ul>
<li>Send one message to someone you have not spoken to in a while. It does not need to be clever.</li>
<li>Ask one real question and listen to the whole answer.</li>
<li>Show up repeatedly to the same place. Friendship tends to grow from repeated, low-pressure contact: a class, a group, a regular walk.</li>
<li>Be the one who suggests a specific plan. "Coffee Saturday at ten?" beats "we should catch up."</li>
<li>Let yourself be seen a little. Brené Brown's talk on vulnerability, in the <a href="/watch/">Watch</a> section, is a good companion.</li>
</ul>
<h2>When it is heavier</h2>
<p>If loneliness comes with persistent low mood or hopelessness, a counselor or a support group can help. The <a href="/help/">help page</a> lists starting points.</p>
""",
"sources": [
  "Robert Waldinger and Marc Schulz, The Good Life: Lessons from the World's Longest Scientific Study of Happiness (2023).",
],
},
{
"slug": "journaling",
"title": "Journaling",
"tags": ["Journaling", "Self-compassion", "Reflection"],
"summary": "Writing about what is going on, privately and without polishing, helps many people think more clearly and feel more settled.",
"read": 3,
"short": [
  "Expressive writing has modest but real benefits in many studies.",
  "Three good things and an evening review are simple formats to start with.",
  "Keep it private and imperfect.",
],
"try": "evening-review",
"practices": ["evening-review", "worry-sort"],
"related": ["self-compassion", "values", "stoic-control"],
"body": """
<h2>The research</h2>
<p>James Pennebaker and colleagues began the modern study of expressive writing in the 1980s. In the classic format, people write about something emotionally difficult for fifteen to twenty minutes on a few consecutive days. A 2006 meta-analysis by Joanne Frattaroli found small but reliable benefits on a range of wellbeing and health outcomes. The effect is not magic and does not work equally for everyone, but it is cheap and low-risk for most people.</p>
<h2>Formats to try</h2>
<ul>
<li><strong>Brain dump.</strong> Five minutes, no editing, everything in your head onto the page.</li>
<li><strong>Expressive writing.</strong> Pick one hard thing and write honestly about it for fifteen minutes, three or four days in a row.</li>
<li><strong>Three good things.</strong> Each evening, write three things that went well and why. A well-known 2005 study by Martin Seligman and colleagues found this simple exercise raised happiness for months.</li>
<li><strong>Evening review.</strong> An old practice: Seneca described asking himself each night what he did well, what he did badly, and what he could do better. Benjamin Franklin did something similar. See {practice:evening-review}.</li>
</ul>
<h2>Making it stick</h2>
<ul>
<li>Keep it private. Writing for an imagined audience changes what you say.</li>
<li>Do not fix the grammar. Nobody is grading.</li>
<li>Pair it with an existing habit, like the end of the evening or the morning coffee.</li>
<li>If writing about something painful leaves you worse for more than a day or two, ease off or talk to someone.</li>
</ul>
""",
"sources": [
  "Frattaroli, 'Experimental disclosure and its moderators: A meta-analysis,' Psychological Bulletin (2006).",
  "Pennebaker, Opening Up: The Healing Power of Expressing Emotions (1997).",
  "Seligman, Steen, Park and Peterson, 'Positive psychology progress: Empirical validation of interventions,' American Psychologist (2005).",
],
},
]

# ---------------------------------------------------------------- PRACTICES
PRACTICES = [
{
"slug": "box-breathing",
"title": "Box breathing",
"minutes": 4,
"summary": "A steady four-count breath that gives a racing mind something simple to do.",
"when": "Before something stressful, when you feel keyed up, or any time you need to slow down.",
"steps": [
  "Sit or stand with your back supported. Let your shoulders drop.",
  "Breathe in through your nose for a count of four.",
  "Hold gently for four.",
  "Breathe out slowly for four.",
  "Hold the empty breath for four.",
  "Repeat for two to four minutes. If you feel dizzy, stop and breathe normally.",
],
"why": "A slow, even rhythm and a longer attention span on one simple task can calm the body's alarm response.",
"pacer": "box",
"ideas": ["urges", "stoic-control"],
},
{
"slug": "cyclic-sigh",
"title": "The cyclic sigh",
"minutes": 3,
"summary": "Two quick breaths in, one long breath out. A fast way to settle.",
"when": "When you are wound up and want relief in under two minutes.",
"steps": [
  "Breathe in through your nose until your lungs are mostly full.",
  "Sneak in a second short sip of air on top to fill them completely.",
  "Let out a long, slow breath through your mouth, longer than the inhale.",
  "Repeat for one to three minutes.",
  "Stop and breathe normally if you feel lightheaded.",
],
"why": "In a 2023 study from Stanford, five minutes a day of cyclic sighing improved mood more than mindfulness meditation did, and lowered breathing rate over a month.",
"pacer": "sigh",
"ideas": ["urges", "attention"],
"source": "Balban et al., 'Brief structured respiration practices enhance mood and reduce physiological arousal,' Cell Reports Medicine (2023).",
},
{
"slug": "grounding-54321",
"title": "5-4-3-2-1 grounding",
"minutes": 2,
"summary": "Use your senses to come back to the room you are actually in.",
"when": "When your thoughts are spiraling or you feel unreal or overwhelmed.",
"steps": [
  "Look around and name five things you can see.",
  "Notice four things you can feel: your feet on the floor, the chair, your clothes, the air.",
  "Listen for three things you can hear.",
  "Find two things you can smell, or recall two smells you like.",
  "Name one thing you can taste, or take a slow sip of water.",
  "Take one slow breath and notice how your body feels now.",
],
"why": "Attention is limited. Pointing it at present-moment sensory detail leaves less room for runaway thoughts.",
"ideas": ["urges", "attention"],
},
{
"slug": "urge-surfing",
"title": "Urge surfing",
"minutes": 10,
"summary": "Ride out a craving by watching it rise and fall instead of obeying or fighting it.",
"when": "When you feel a strong pull to do something you do not want to do.",
"steps": [
  "Stop, and say to yourself, \"This is an urge.\" You do not have to act on it.",
  "Get comfortable. Close your eyes or soften your gaze.",
  "Scan your body. Where do you feel it? Chest, throat, stomach, hands? Describe the sensation as if to a scientist: tight, hot, buzzing, hollow.",
  "Breathe slowly. Imagine the urge as a wave. Watch it grow, crest, and begin to fall.",
  "When thoughts show up (\"I can't stand this\"), label them as thoughts and return to the body.",
  "Stay until the wave has clearly dropped. Then do something different with your hands and feet: walk, wash your face, call someone.",
  "Afterward, jot down what happened right before the urge. Patterns show up quickly.",
],
"why": "Urges are temporary. Watching one pass without acting teaches your brain that you can survive it.",
"ideas": ["urges", "habits", "self-compassion"],
},
{
"slug": "values-check",
"title": "Values check",
"minutes": 5,
"summary": "Find the direction you actually care about, then pick one small step.",
"when": "When you feel lost, stuck, or pulled in too many directions.",
"steps": [
  "Draw four boxes on a page: Relationships, Work or craft, Health, Meaning or community.",
  "In each box, write one sentence about how you would like to show up. Not what you will achieve, but who you want to be.",
  "Circle the one that feels most neglected right now.",
  "Write one small action this week that lives in that direction. Make it something you could do in under twenty minutes.",
  "Put it on your calendar with a time.",
],
"why": "Values are a compass that keeps working even when goals fall apart. A small action turns the compass into movement.",
"ideas": ["values", "feeling-lost"],
},
{
"slug": "two-minute-start",
"title": "The two-minute start",
"minutes": 2,
"summary": "Shrink the first step until it is too small to resist.",
"when": "When you are avoiding something and cannot get going.",
"steps": [
  "Name the thing you are avoiding in one line.",
  "Ask: what is a version of this I could do in two minutes? Open the document. Put on the shoes. Write the first sentence. Send the one-line text.",
  "Do only that. Set a timer if it helps.",
  "When the two minutes end, you are allowed to stop. Many people keep going. Either way you have started, and starting is the hard part.",
],
"why": "The dread usually peaks before beginning. A tiny first step skips past it and builds momentum.",
"ideas": ["procrastination", "discipline", "habits"],
},
{
"slug": "if-then-plan",
"title": "Build an if-then plan",
"minutes": 5,
"summary": "Decide in advance when and where you will act, so the moment does not require willpower.",
"when": "When you keep intending to do something and keep not doing it, or when you want to block an old reflex.",
"steps": [
  "Pick one behavior to start or one reflex to interrupt.",
  "Choose a cue that reliably happens: a time, a place, a finished task, a particular feeling.",
  "Write the plan in one line: \"If [cue], then I will [small action].\"",
  "Make the action concrete and small. \"Walk to the corner\" beats \"get more exercise.\"",
  "Say it out loud once. Put it where you will see it.",
  "After a week, adjust the cue or the action if it is not working.",
],
"why": "Linking a specific cue to a specific action hands control to the situation instead of requiring a decision each time.",
"ideas": ["if-then", "habits", "discipline"],
},
{
"slug": "evening-review",
"title": "Evening review",
"minutes": 5,
"summary": "A short, kind look back at the day, in the spirit of Seneca.",
"when": "At the end of the day, before bed or before you open your phone for the night.",
"steps": [
  "Write down one thing that went well, and why.",
  "Write down one thing you would do differently. Describe it plainly, without judgment.",
  "Write down one thing you are grateful for.",
  "Ask: what is one small step toward what matters tomorrow? Write it down.",
  "End with one kind sentence to yourself, the one you would say to a friend.",
],
"why": "Reviewing the day turns experience into learning, and ending kindly keeps you willing to come back to the practice.",
"ideas": ["journaling", "self-compassion", "values"],
},
{
"slug": "body-scan",
"title": "Body scan",
"minutes": 10,
"summary": "Slowly move your attention through the body, noticing without fixing.",
"when": "When you are tense, tired, or lying awake. Also good as a daily anchor.",
"steps": [
  "Lie down or sit comfortably. Close your eyes if that feels okay.",
  "Take three slow breaths.",
  "Bring attention to your feet. Notice any sensation: warmth, pressure, tingling, nothing at all.",
  "Move slowly upward: ankles, calves, knees, thighs, hips, belly, chest, hands, arms, shoulders, neck, face, scalp.",
  "At each place, just notice. You are not trying to relax anything, only to feel.",
  "If your mind wanders, which it will, gently return to the last place you remember.",
  "Finish with a few breaths feeling the whole body at once.",
],
"why": "Learning to feel the body as it is builds the skill of noticing urges and emotions before they take over. The method is central to Jon Kabat-Zinn's stress-reduction program.",
"ideas": ["body-foundation", "self-compassion"],
"guided": "body-scan",
},
{
"slug": "phone-free-walk",
"title": "Phone-free walk",
"minutes": 15,
"summary": "Walk with no audio, no screen, and no destination.",
"when": "When you feel scattered, stuck on a problem, or restless.",
"steps": [
  "Leave your phone behind, or put it in a bag on airplane mode.",
  "Walk for at least fifteen minutes. Pick any route.",
  "Let your attention drift to what is around you: light, sounds, the feeling of your feet.",
  "When boredom or the urge to check something appears, notice it and keep walking.",
  "If a problem is on your mind, let it float along with you without forcing an answer.",
],
"why": "Walking helps mood, and a 2014 Stanford study found that people generated more creative ideas while walking than while sitting. A little boredom builds your tolerance for it.",
"ideas": ["attention", "body-foundation"],
"source": "Oppezzo and Schwartz, 'Give your ideas some legs: The positive effect of walking on creative thinking,' Journal of Experimental Psychology: Learning, Memory, and Cognition (2014).",
},
{
"slug": "worry-sort",
"title": "Worry sort",
"minutes": 5,
"summary": "Split your worries into what is up to you and what is not.",
"when": "When your head is full of what-ifs.",
"steps": [
  "Write every worry on a page, one per line. Do not edit.",
  "Draw a line down the middle. Label the left column \"Up to me\" and the right column \"Not up to me.\"",
  "Move each worry into a column. Be honest. Other people's opinions, the future, and results usually go on the right.",
  "For each item on the left, write one small action you can take, or write \"nothing now.\"",
  "For each item on the right, write one sentence of release, such as \"I will do my part and let the rest be.\"",
  "Do the first action on the left, or schedule it.",
],
"why": "Sorting turns a formless cloud of anxiety into a short to-do list and a few things to let go of. It is the Stoic dichotomy of control in practice.",
"ideas": ["stoic-control", "journaling"],
},
]

# ---------------------------------------------------------------- GUIDED SCRIPTS
SCRIPTS = [
{
"id": "body-scan",
"title": "Body scan",
"minutes": "About 8 minutes",
"lines": [
  "Find a comfortable position, sitting or lying down. Let your eyes close, or rest them on a spot in front of you.",
  "Take a slow breath in through your nose, and let it go with a long sigh. Do that two more times.",
  "Now bring your attention to your feet. Notice whatever is there: warmth, coolness, pressure, tingling, or nothing. Nothing is fine.",
  "Let your attention travel up through your ankles and calves. You are not trying to change anything. Just noticing.",
  "Move to your knees and thighs. Feel the weight of your legs resting where they rest.",
  "Notice your hips and lower back. Breathe into any place that feels tight, without forcing it to let go.",
  "Bring attention to your belly. Feel it rise and fall with each breath.",
  "Notice your chest, and the rhythm of your heart if you can feel it. Then your shoulders. Let them drop a little.",
  "Feel your hands and arms, all the way from fingertips to shoulders.",
  "Notice your neck, your jaw, your face. Soften the muscles around your eyes and mouth.",
  "If your mind has wandered, and it probably has, that is completely normal. Just return to the last place you remember.",
  "Now feel your whole body at once, breathing. Rest here for a few breaths.",
  "When you are ready, wiggle your fingers and toes, and open your eyes.",
],
},
{
"id": "loving-kindness",
"title": "Loving-kindness",
"minutes": "About 7 minutes",
"lines": [
  "Settle into a comfortable position. Take a few slow breaths.",
  "Bring to mind someone who makes you smile easily. A friend, a child, a pet. Picture them and notice the warmth that arises.",
  "Silently offer them these wishes, slowly: May you be safe. May you be healthy. May you be happy. May you live with ease.",
  "Now turn the same wishes toward yourself. This can feel awkward, and that is okay. May I be safe. May I be healthy. May I be happy. May I live with ease.",
  "If it helps, place a hand on your chest and feel its warmth as you say the words.",
  "Now bring to mind someone neutral, like a neighbor or a cashier you see sometimes. Offer them the same wishes.",
  "If you feel ready, bring to mind someone you find difficult. You do not have to like them. Simply wish them the same things, and stop whenever it is too much.",
  "Finally, widen the circle. May all beings be safe. May all beings be healthy. May all beings be happy. May all beings live with ease.",
  "Rest for a moment in whatever you feel, then gently open your eyes.",
],
},
{
"id": "noting",
"title": "Noting thoughts",
"minutes": "About 6 minutes",
"lines": [
  "Sit comfortably and take a few slow breaths. Let your attention rest on the feeling of breathing, wherever you feel it most clearly.",
  "Thoughts will come. When one does, silently give it a simple label: planning, remembering, worrying, judging, or just thinking.",
  "Do not argue with the thought, and do not follow it. Label it lightly, like putting a sticky note on a box, then return to the breath.",
  "If a feeling comes, label that too: sadness, restlessness, boredom, anxiety, calm.",
  "If a sound or a sensation pulls you away, note it as hearing or feeling and come back.",
  "You are not trying to have fewer thoughts. You are learning to see them as passing events, not commands.",
  "Keep noting and returning for a few minutes. Every return is the practice working.",
  "When you are ready, take one deeper breath and open your eyes.",
],
},
]

# ---------------------------------------------------------------- WATCH
# (youtube id, title, speaker, minutes, note)
TALKS = [
{"id": "UF8uR6Z6KLc", "title": "Stanford Commencement Address", "who": "Steve Jobs (2005)", "min": 15,
 "note": "Three stories about connecting the dots, losing what you love, and mortality as a clarifier."},
{"id": "arj7oStGLkU", "title": "Inside the Mind of a Master Procrastinator", "who": "Tim Urban, TED", "min": 14,
 "note": "Funny and uncomfortably accurate. Ends with a sobering look at how many weeks we have."},
{"id": "RcGyVTAoXEU", "title": "How to Make Stress Your Friend", "who": "Kelly McGonigal, TED", "min": 14,
 "note": "A health psychologist on how our beliefs about stress may shape its effects. A view worth weighing; research on stress mindset is still developing."},
{"id": "H14bBuluwB8", "title": "Grit: The Power of Passion and Perseverance", "who": "Angela Duckworth, TED", "min": 6,
 "note": "A short, influential talk. Watch it alongside the criticism: a 2017 meta-analysis (Credé and colleagues) found grit overlaps heavily with conscientiousness."},
{"id": "iCvmsMzlF7o", "title": "The Power of Vulnerability", "who": "Brené Brown, TEDxHouston", "min": 20,
 "note": "On shame, connection, and why letting yourself be seen is part of a full life."},
]
LONG_TALKS = [
{"url": "https://www.youtube.com/watch?v=3nwwKbM_vJc", "title": "Mindfulness, Stress Reduction and Healing (Google Tech Talk, 2007)", "who": "Jon Kabat-Zinn", "min": 72,
 "note": "The founder of mindfulness-based stress reduction explains the practice and leads a short meditation."},
{"url": "https://www.learnoutloud.com/Free-Audio-Video/Science/-/Human-Behavioral-Biology/161370", "title": "Human Behavioral Biology (Stanford course)", "who": "Robert Sapolsky", "min": None,
 "note": "A free university course on the biology behind why we do what we do. Link goes to a listing of the lectures."},
]
CHANNELS = [
{"url": "https://www.youtube.com/channel/UCcv7KJIAsiddB2YRegvrF7g", "title": "Plum Village", "note": "Guided meditations and talks from the community of Thich Nhat Hanh. Also free as the Plum Village app."},
{"url": "https://www.youtube.com/channel/UCnXA5htGOTCxc67ASZkPtcg", "title": "Ram Dass", "note": "Official channel with talks on love, service, aging, and awareness."},
]

# ---------------------------------------------------------------- READ
FREE_BOOKS = [
{"url": "https://standardebooks.org/ebooks/marcus-aurelius/meditations/george-long", "title": "Meditations", "who": "Marcus Aurelius",
 "note": "A Roman emperor's private notes to himself on staying steady. Free, well-formatted edition."},
{"url": "https://www.gutenberg.org/ebooks/45109", "title": "The Enchiridion", "who": "Epictetus",
 "note": "A short handbook of Stoic practice, starting with what is and is not up to you."},
{"url": "https://standardebooks.org/ebooks/seneca/dialogues/aubrey-stewart/text/on-the-shortness-of-life", "title": "On the Shortness of Life", "who": "Seneca",
 "note": "An essay arguing life is long enough if we stop wasting it. Short and blunt."},
{"url": "https://standardebooks.org/ebooks/seneca/moral-letters-to-lucilius/richard-m-gummere/text", "title": "Moral Letters to Lucilius", "who": "Seneca",
 "note": "Letters of practical advice from an older man to a younger friend."},
{"url": "https://www.gutenberg.org/ebooks/4507", "title": "As a Man Thinketh", "who": "James Allen",
 "note": "A 1903 essay on how thought shapes character. Short, earnest, and a root of much modern self-help."},
{"url": "https://psychclassics.yorku.ca/James/Principles/prin4.htm", "title": "Habit (chapter from The Principles of Psychology)", "who": "William James",
 "note": "The 1890 chapter that still reads like good advice on building and breaking habits."},
]
ENCYCLOPEDIA = [
{"url": "https://en.wikipedia.org/wiki/Stoicism", "title": "Stoicism"},
{"url": "https://en.wikipedia.org/wiki/Habit", "title": "Habit"},
{"url": "https://en.wikipedia.org/wiki/Acceptance_and_commitment_therapy", "title": "Acceptance and commitment therapy"},
{"url": "https://en.wikipedia.org/wiki/Implementation_intention", "title": "Implementation intention"},
{"url": "https://en.wikipedia.org/wiki/Self-compassion", "title": "Self-compassion"},
{"url": "https://en.wikipedia.org/wiki/Procrastination", "title": "Procrastination"},
{"url": "https://en.wikipedia.org/wiki/Ikigai", "title": "Ikigai"},
]

# ---------------------------------------------------------------- MEDITATE (external audio)
MEDITATE_LINKS = [
{"url": "https://www.uclahealth.org/programs/marc/free-guided-meditations/guided-meditations", "title": "UCLA Mindful Awareness Research Center",
 "note": "Free guided meditations from three to nineteen minutes, with transcripts. Several languages."},
{"url": "https://plumvillage.app/", "title": "Plum Village app",
 "note": "A free app of guided meditations, talks, and chants from the Plum Village tradition."},
{"url": "https://www.youtube.com/channel/UCcv7KJIAsiddB2YRegvrF7g", "title": "Plum Village on YouTube",
 "note": "Includes the popular 'Calm and Ease' guided meditation in several lengths."},
]

# ---------------------------------------------------------------- SHOP
FREE_FIRST = [
{"title": "A library card", "note": "Almost every book below is at a public library, often as a free ebook or audiobook through an app like Libby."},
{"title": "Plum Village and UCLA Mindful apps", "note": "Free, high-quality guided meditation. See the Meditate page."},
{"title": "A notebook you already own", "note": "Journaling works the same on any paper. Do not buy gear before you have a habit."},
]
PRODUCTS = [
 ("Books", [
  ("Atomic Habits", "James Clear", "Atomic Habits James Clear", "A practical, readable guide to building habits through small changes and environment design."),
  ("Man's Search for Meaning", "Viktor Frankl", "Man's Search for Meaning Viktor Frankl", "A psychiatrist's account of surviving the camps and the idea that meaning is something we choose toward."),
  ("Meditations", "Marcus Aurelius, trans. Gregory Hays", "Meditations Marcus Aurelius Gregory Hays", "The most readable modern translation of a Stoic classic. The free Long translation is on the Read page."),
  ("The Happiness Trap", "Russ Harris", "The Happiness Trap Russ Harris", "A friendly introduction to Acceptance and Commitment Therapy, with exercises."),
  ("Self-Compassion", "Kristin Neff", "Self-Compassion Kristin Neff", "The researcher's own guide to being kinder to yourself without losing your edge."),
  ("Deep Work", "Cal Newport", "Deep Work Cal Newport", "A case and a plan for protecting long stretches of focused work."),
  ("Four Thousand Weeks", "Oliver Burkeman", "Four Thousand Weeks Oliver Burkeman", "A thoughtful, funny rethink of time management that begins with accepting limits."),
  ("Full Catastrophe Living", "Jon Kabat-Zinn", "Full Catastrophe Living Jon Kabat-Zinn", "The foundational book of mindfulness-based stress reduction."),
  ("The Good Life", "Robert Waldinger and Marc Schulz", "The Good Life Waldinger Schulz", "What the world's longest study of adult life says about relationships and wellbeing."),
  ("Working Identity", "Herminia Ibarra", "Working Identity Herminia Ibarra", "For anyone in a career or life transition who cannot plan their way out."),
 ]),
 ("Simple tools", [
  ("A good notebook", "Dotted or lined, your choice", "Leuchtturm1917 dotted notebook", "A sturdy notebook you actually enjoy opening makes journaling easier to start."),
  ("A meditation cushion", "Zafu or similar", "zafu meditation cushion", "Optional. A firm cushion makes it easier to sit comfortably for ten minutes."),
  ("A visual timer", "Time Timer or similar", "Time Timer visual timer", "Shows time as a shrinking disc. Helpful for timed focus blocks and the two-minute start."),
  ("A sunrise alarm clock", "Wake-up light", "wake-up light sunrise alarm clock", "Gradual light can make waking easier, especially in dark months."),
  ("A phone lock box", "Timer-lock container", "phone lock box timer container", "Puts the phone physically out of reach for a set time. Blunt and effective."),
  ("Resistance bands", "Basic set", "resistance bands set", "Cheap, quiet, and good for short movement breaks at home."),
 ]),
]

SOUNDS_TRUE = {
  "title": "Sounds True",
  "who": "Courses and audio programs",
  "url": SOUNDSTRUE,
  "why": "Audio and video courses from meditation and spiritual teachers, including Jack Kornfield, Michael Singer, and Eckhart Tolle. Paid, and worth it only if you want a guided, longer program. Many of these teachers also have free talks on the Watch page.",
}
