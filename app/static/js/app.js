// MediTrack Main JavaScript Engine & Bilingual Translation Engine (বাংলা <-> English)

const i18n = {
    bn: {
        lang_name: "English",
        
        // Navigation & Top Bar
        emergency_notice: "🇧🇩 বাংলাদেশ স্বাস্থ্য ও ওষুধ ট্র্যাকিং প্ল্যাটফর্ম (MediTrack Bangladesh)",
        helpline_health: "জরুরি স্বাস্থ্য সেবা: ১৬২৬৩",
        helpline_national: "জাতীয় জরুরি সেবা: ৯৯৯",
        nav_brand_sub: "বিডি কেয়ার",
        nav_dashboard: "📊 ড্যাশবোর্ড",
        nav_medications: "💊 ওষুধের রুটিন",
        nav_doctors: "👨‍⚕️ ডাক্তার ও চেম্বার",
        nav_appointments: "🗓️ সিরিয়াল ও ভিজিট",
        nav_prescriptions: "📁 প্রেসক্রিপশন ফাইল",
        nav_family: "👨‍👩‍👧 পরিবার",
        nav_admin: "⚙️ অ্যাডমিন",
        nav_ramadan: "রমজান মোড",
        nav_ramadan_title: "রোজার সময়ে ওষুধের সময়সূচী পরিবর্তন করুন",
        nav_login: "লগইন",
        nav_register: "রেজিস্ট্রেশন",
        nav_logout_title: "লগআউট",
        
        // Footer
        footer_rights: "© 2026 MediTrack Bangladesh. All rights reserved.",
        footer_disclaimer: "মেডিট্র্যাক শুধুমাত্র ওষুধ ও ফলো-আপ সংরক্ষণের সহায়ক ডিজিটাল প্ল্যাটফর্ম।",
        footer_feat_bilingual: "🌐 দ্বৈত ভাষা (বাংলা / English)",
        footer_feat_bmdc: "✓ BMDC ভেরিফাইড তথ্য",
        footer_feat_caregiver: "👨‍👩‍👧 সহজ কেয়ারগিভার ট্র্যাকিং",

        // Landing Page (Index)
        home_badge: "বাংলাদেশের স্বাস্থ্যব্যবস্থা ও প্রেসক্রিপশন সংস্কৃতির জন্য বিশেষায়িত",
        home_title: "সময়মতো সঠিক ওষুধ সেবন ও চিকিৎসকের চেম্বার ট্র্যাকিং এখন সহজ",
        home_desc: "প্রেসক্রিপশনের কাগজ হারিয়ে যাওয়া কিংবা বাবা-মায়ের ডায়াবেটিস ও প্রেসারের ওষুধের সময়সূচি মনে রাখার ঝামেলা দূর করুন। ১+০+১ নিয়ম, খাওয়ার আগে/পরে এবং প্রাইভেট চেম্বার সিরিয়াল—সবকিছু এক প্ল্যাটফর্মে।",
        home_btn_demo: "🚀 ডেমো অ্যাকাউন্ট দিয়ে ব্যবহার করুন",
        home_btn_register: "নতুন অ্যাকাউন্ট তৈরি করুন",
        home_feat_pharma: "✓ দেশীয় ফার্মা ব্র্যান্ড (Napa, Seclo, Monas)",
        home_feat_caregiver: "✓ পরিবার ও বয়স্কদের কেয়ারগিভার ট্র্যাকিং",
        home_feat_chamber: "✓ জনপ্রিয় চেম্বার ও সিরিয়াল ডিরেক্টরি",
        home_card1_icon: "১+০+১",
        home_card1_title: "দেশীয় প্রেসক্রিপশন রুটিন",
        home_card1_desc: "বাংলাদেশের চিকিৎসকদের ১+০+১ কিংবা ১+১+১ নিয়ম এবং \"খাওয়ার আগে\", \"ভরা পেটে\" বা \"শোবার আগে\" সময়সূচী সহজে সেট করুন। রমজান মাসে স্বয়ংক্রিয় সেহরি-ইফতার মোড।",
        home_card2_icon: "👨‍👩‍👧",
        home_card2_title: "বাবা-মায়ের কেয়ারগিভার ট্র্যাকিং",
        home_card2_desc: "কর্মজীবী সন্তানেরা সহজেই দূরে থেকেও বাবা-মা বা পরিবারের সদস্যদের ডায়াবেটিস ও প্রেসারের ওষুধ সময়মতো খাওয়া হয়েছে কি না তা এক ক্লিকে নজর রাখতে পারবেন।",
        home_card3_icon: "🏥",
        home_card3_title: "প্রাইভেট চেম্বার ও সিরিয়াল",
        home_card3_desc: "পপুলার, ইবনে সিনা, ল্যাবএইডসহ ঢাকা ও প্রধান শহরের বিশেষজ্ঞ চিকিৎসকদের চেম্বার ঠিকানা, ভিজিটিং সময় এবং সিরিয়াল ফোন নম্বর সহজে খুঁজুন ও সংরক্ষণ করুন।",
        home_demo_badge: "⚡ তাৎক্ষণিক টেস্ট ক্রেডেনশিয়াল",
        home_demo_title: "এক ক্লিকেই পরীক্ষা করতে লগইন করুন",
        home_demo_desc: "ইমেইল: demo@meditrack.bd | পাসওয়ার্ড: password123",
        home_demo_admin: "(অ্যাডমিন প্যানেল: admin@meditrack.bd / admin123)",
        home_demo_btn: "লগইন পেজে যান →",

        // Dashboard
        dash_age_suffix: "বছর",
        dash_add_med: "➕ নতুন ওষুধ যুক্ত করুন",
        dash_find_doc: "ডাক্তার খুঁজুন",
        dash_ramadan_notice_title: "রমজান মোড সক্রিয়:",
        dash_ramadan_notice_desc: "দুপুরের নিয়মিত ওষুধ চিকিৎসকের পরামর্শ অনুযায়ী সেহরি ও ইফতারের সময়ে সমন্বয় করে গ্রহণ করুন।",
        dash_total_doses: "আজকের মোট ডোজ",
        dash_total_sub: "নির্ধারিত সময়মতো সেবন",
        dash_taken: "গৃহীত (Taken)",
        dash_taken_sub: "সফলভাবে গৃহীত ডোজ",
        dash_missed: "বাদ পড়েছে (Missed)",
        dash_missed_sub: "ভুলে যাওয়া বা বাদ পড়া ডোজ",
        dash_adherence: "৭ দিনের সফলতার হার",
        dash_schedule_title: "🕒 আজকের ওষুধের সময়সূচী ও ট্র্যাকিং",
        dash_today: "আজ",
        dash_loading_meds: "ওষুধের তথ্য লোড হচ্ছে...",
        dash_upcoming_serial: "পরবর্তী চেম্বার সিরিয়াল",
        dash_view_all: "সবগুলো দেখুন →",
        dash_serial_label: "সিরিয়াল:",
        dash_datetime_label: "তারিখ ও সময়:",
        dash_chamber_call: "📞 চেম্বারে কল করুন",
        dash_no_serial: "বর্তমানে কোনো আসন্ন ডাক্তারের সিরিয়াল নেই।",
        dash_book_serial_btn: "চেম্বার সিরিয়াল বুক করুন",
        dash_chart_title: "৭ দিনের সেবন ধারাবাহিকতা",
        dash_chart_sub: "বার চার্ট",
        dash_helpline_title: "জরুরি মেডিকেল হেল্পলাইন",
        dash_shastho: "স্বাস্থ্য বাতায়ন (২৪/৭ ডাক্তার):",
        dash_national: "জাতীয় জরুরি সেবা (অ্যাম্বুলেন্স):",
        dash_birdem: "বারডেম ডায়াবেটিস হেল্পলাইন:",
        dash_confirmed_at: "সেবনের নিশ্চিত সময়:",
        dash_no_meds: "এই সদস্যের জন্য আজকে কোনো ওষুধের শিডিউল সক্রিয় নেই।",
        dash_add_first_med: "➕ একটি ওষুধ যুক্ত করুন",
        btn_taken: "✓ গৃহীত",
        btn_missed: "✕ বাদ পড়েছে",
        btn_take: "✓ খেয়েছি",
        btn_miss: "✕ বাদ",

        // Slots
        slot_morning_title: "🌅 সকালের ওষুধ (Morning)",
        slot_afternoon_title: "☀️ দুপুরের ওষুধ (Afternoon)",
        slot_night_title: "🌙 রাতের খাবার ও ওষুধ (Night)",
        slot_bedtime_title: "🛌 রাতে শোবার আগে (Bedtime)",
        slot_sos_title: "⚡ প্রয়োজনে (SOS)",
        slot_morning_time: "০৮:০০ AM",
        slot_afternoon_time: "০২:০০ PM",
        slot_night_time: "০৯:৩০ PM",
        slot_bedtime_time: "১১:০০ PM",
        slot_sos_time: "প্রয়োজনে",

        // Medications Page
        meds_page_title: "ওষুধের তালিকা ও সময়সূচী",
        meds_active_member_prefix: "নির্বাচিত সদস্য:",
        meds_btn_add: "➕ নতুন ওষুধ যুক্ত করুন",
        meds_section_title: "💊 নিয়মিত ও চলমান ওষুধসমূহ",
        meds_count_suffix: "টি ওষুধ তালিকাভুক্ত",
        meds_chronic_badge: "✓ নিয়মিত / দীর্ঘমেয়াদী",
        meds_generic_label: "জেনেরিক:",
        meds_prescriber_label: "👨‍⚕️ পরামর্শক:",
        meds_start_date: "📅 শুরু:",
        meds_end_date: "শেষ:",
        meds_status_active: "চলমান",
        meds_status_paused: "স্থগিত",
        meds_delete_tooltip: "মুছে ফেলুন",
        meds_empty_text: "কোনো ওষুধ যুক্ত করা হয়নি।",
        meds_empty_btn: "প্রথম ওষুধটি যুক্ত করুন",
        meds_modal_title: "💊 নতুন ওষুধ যুক্ত করুন",
        meds_name_label: "ওষুধের নাম (ব্র্যান্ড / জেনেরিক খুঁজুন)",
        meds_name_placeholder: "যেমনঃ Napa Extra, Seclo 20, Monas 10...",
        meds_generic_label_form: "জেনেরিক নাম (ঐচ্ছিক)",
        meds_generic_placeholder: "Paracetamol, Omeprazole...",
        meds_form_label: "ওষুধের ধরন",
        meds_form_tablet: "ট্যাবলেট (Tablet)",
        meds_form_capsule: "ক্যাপসুল (Capsule)",
        meds_form_syrup: "সিরাপ (Syrup)",
        meds_form_inhaler: "ইনহেলার (Inhaler)",
        meds_form_drop: "ড্রপ (Drop)",
        meds_form_injection: "ইনজেকশন (Injection)",
        meds_pattern_label: "প্রেসক্রিপশন ডোজের নিয়ম",
        meds_pattern_101: "১+০+১ (সকালে ১টি ও রাতে ১টি)",
        meds_pattern_111: "১+১+১ (সকাল, দুপুর ও রাত)",
        meds_pattern_100: "১+০+০ (শুধু সকালে)",
        meds_pattern_010: "০+১+০ (শুধু দুপুরে)",
        meds_pattern_001: "০+০+১ (শুধু রাতে)",
        meds_pattern_1001: "১+০+০+১ (সকাল ও রাতে শোবার আগে)",
        meds_pattern_sos: "SOS (প্রয়োজনে / ব্যথা হলে)",
        meds_meal_label: "খাবার সাথে সম্পর্কিত নিয়ম",
        meds_meal_after: "খাওয়ার পরে (After Meal)",
        meds_meal_before: "খাওয়ার ২০ মিনিট আগে (Before Meal)",
        meds_meal_empty: "খালি পেটে (Empty Stomach)",
        meds_meal_bedtime: "রাতে শোবার আগে (At Bedtime)",
        meds_start_label: "শুরুর তারিখ",
        meds_doctor_label: "ডাক্তারের নাম",
        meds_doctor_placeholder: "প্রেসক্রাইবার ডাক্তার",
        meds_chronic_check: "নিয়মিত ওষুধ (প্রেসার/সুগারের দীর্ঘস্থায়ী কোর্স)",
        meds_instructions_label: "বিশেষ নির্দেশনা / ডাক্তারের নোট",
        meds_instructions_placeholder: "যেমনঃ পর্যাপ্ত পানি খাবেন, চিনি এড়িয়ে চলবেন...",
        btn_cancel: "বাতিল",
        btn_save: "সংরক্ষণ করুন",
        meds_confirm_delete: "আপনি কি এই ওষুধটি তালিকা থেকে মুছে ফেলতে চান?",
        meds_toast_added: "ওষুধ সফলভাবে যুক্ত হয়েছে!",
        meds_toast_status: "স্ট্যাটাস পরিবর্তন করা হয়েছে",
        meds_toast_deleted: "ওষুধটি মুছে ফেলা হয়েছে",

        // Doctor Directory
        doc_bmdc_badge: "🇧🇩 BMDC নিবন্ধিত বিশেষজ্ঞ ডাক্তার",
        doc_banner_title: "বাংলাদেশ স্পেশালিস্ট ও চেম্বার ডিরেক্টরি",
        doc_banner_sub: "ঢাকা, চট্টগ্রাম ও প্রধান শহরসমূহের স্বনামধন্য বিশেষজ্ঞ চিকিৎসক ও ডায়াগনস্টিক সেন্টারের চেম্বার তথ্য ও সিরিয়াল হটলাইন।",
        doc_search_label: "ডাক্তার বা চেম্বার খুঁজুন",
        doc_search_placeholder: "নাম, পপুলার, ইবনে সিনা...",
        doc_div_label: "বিভাগ (Division)",
        doc_div_all: "সকল বিভাগ (All)",
        doc_area_label: "এলাকা / থানা (Area)",
        doc_area_all: "সকল এলাকা (All)",
        doc_spec_label: "বিশেষজ্ঞ বিভাগ (Specialty)",
        doc_spec_all: "সকল বিশেষজ্ঞ (All)",
        doc_spec_med: "মেডিসিন ও ডায়াবেটিস",
        doc_spec_cardio: "কার্ডিওলজি ও হৃদরোগ",
        doc_spec_neuro: "নিউরোমেডিসিন",
        doc_spec_pedia: "শিশু বিশেষজ্ঞ",
        doc_spec_ortho: "অর্থোপেডিক ও হাড়",
        doc_spec_nephro: "কিডনি রোগ বিশেষজ্ঞ",
        doc_search_btn: "🔍 অনুসন্ধান করুন",
        doc_loading: "ডাক্তার তালিকা লোড হচ্ছে...",
        doc_not_found: "কোনো ডাক্তার পাওয়া যায়নি। অন্য ফিল্টার ব্যবহার করে চেষ্টা করুন।",
        doc_visiting_time: "ভিজিটিং সময়:",
        doc_fee: "ফি:",
        doc_save_serial: "🗓️ সিরিয়াল সংরক্ষণ",
        doc_call_prefix: "📞 কল",
        doc_modal_title: "🗓️ ডাক্তারের চেম্বার সিরিয়াল যুক্ত করুন",
        doc_patient_name: "রোগীর নাম (পরিবার সদস্য)",
        doc_name_label: "ডাক্তারের নাম",
        doc_chamber_label: "চেম্বার ও ঠিকানা",
        doc_date_label: "সাক্ষাতের তারিখ",
        doc_time_label: "সময় (Time)",
        doc_time_placeholder: "০৬:৩০ PM",
        doc_serial_no_label: "সিরিয়াল নম্বর",
        doc_serial_no_placeholder: "যেমনঃ Serial #14",
        doc_hotline_label: "সিরিয়াল ফোন নম্বর",
        doc_notes_label: "পরামর্শ / পূর্ববর্তী রিপোর্ট সাথে নেওয়ার নোট",
        doc_notes_placeholder: "যেমনঃ নতুন FBS ও লিপিড প্রোফাইল টেস্ট ফাইল সাথে নেবেন...",
        doc_toast_saved: "সিরিয়াল ও অ্যাপয়েন্টমেন্ট সফলভাবে যুক্ত হয়েছে!",

        // Appointments
        apt_title: "ডাক্তার অ্যাপয়েন্টমেন্ট ও চেম্বার সিরিয়াল",
        apt_patient_prefix: "রোগী:",
        apt_subtitle: "চেম্বার ভিজিট ও ফলো-আপ ট্র্যাকার",
        apt_btn_add: "➕ নতুন চেম্বার সিরিয়াল যুক্ত করুন",
        apt_section_title: "নির্ধারিত ও পূর্ববর্তী চেম্বার ভিজিটসমূহ",
        apt_records_count: "টি রেকর্ড",
        apt_chamber_label: "চেম্বার:",
        apt_date_label: "তারিখ:",
        apt_time_label: "সময়:",
        apt_hotline_label: "হটলাইন:",
        apt_advice_label: "পরামর্শ / নোট:",
        apt_followup_label: "🔄 পরবর্তী ফলো-আপ সাক্ষাত:",
        apt_btn_complete: "✓ সম্পন্ন",
        apt_btn_cancel: "বাতিল",
        apt_empty_text: "কোনো চেম্বার সিরিয়াল বা অ্যাপয়েন্টমেন্ট তালিকাভুক্ত নেই।",
        apt_empty_btn: "ডাক্তার ডিরেক্টরি থেকে সিরিয়াল নিন",
        apt_confirm_delete: "আপনি কি এই অ্যাপয়েন্টমেন্ট রেকর্ডটি মুছে ফেলতে চান?",
        apt_toast_updated: "অ্যাপয়েন্টমেন্ট আপডেট করা হয়েছে",
        apt_toast_deleted: "রেকর্ড মুছে ফেলা হয়েছে",

        // Prescriptions
        rx_title: "ডিজিটাল প্রেসক্রিপশন ও টেস্ট রিপোর্ট ভল্ট",
        rx_subtitle: "প্রেসক্রিপশনের কাগজ হারিয়ে যাওয়া রোধে ছবি সংরক্ষণ করুন",
        rx_print_btn: "🖨️ চেম্বার সামারি প্রিন্ট",
        rx_upload_btn: "📷 প্রেসক্রিপশন আপলোড",
        rx_zoom: "🔍 বড় করে দেখুন",
        rx_view: "দেখুন →",
        rx_delete: "মুছে ফেলুন",
        rx_empty_text: "কোনো প্রেসক্রিপশন বা টেস্ট রিপোর্ট আপলোড করা নেই।",
        rx_empty_btn: "প্রেসক্রিপশনের ছবি আপলোড করুন",
        rx_modal_title: "প্রেসক্রিপশন বা রিপোর্ট আপলোড",
        rx_file_title_label: "ফাইলের শিরোনাম",
        rx_file_title_placeholder: "উদাঃ বিএসএমএমইউ প্রেসক্রিপশন / সিবিসি রিপোর্ট",
        rx_doctor_label: "ডাক্তারের নাম",
        rx_doctor_placeholder: "অধ্যাপক ডাঃ...",
        rx_hospital_label: "হাসপাতাল / ডায়াগনস্টিক সেন্টার",
        rx_hospital_placeholder: "যেমনঃ পপুলার, বারডেম, ডিএমসিএইচ",
        rx_date_label: "তারিখ",
        rx_file_label: "প্রেসক্রিপশনের ছবি বা পিডিএফ ফাইল",
        rx_diag_label: "রোগের বিবরণ বা পরামর্শের সারসংক্ষেপ",
        rx_diag_placeholder: "সংক্ষিপ্ত নোট...",
        rx_btn_upload: "আপলোড করুন",
        rx_preview_title: "প্রেসক্রিপশন প্রিভিউ",
        rx_confirm_delete: "আপনি কি এই প্রেসক্রিপশনটি মুছে ফেলতে চান?",
        rx_toast_uploaded: "প্রেসক্রিপশন সফলভাবে আপলোড হয়েছে!",
        rx_toast_deleted: "প্রেসক্রিপশন মুছে ফেলা হয়েছে",

        // Family
        fam_title: "পরিবার ও কেয়ারগিভার প্রোফাইল",
        fam_subtitle: "একই অ্যাকাউন্ট থেকে নিজের পাশাপাশি বাবা, মা বা পরিবারের যেকোনো সদস্যের স্বাস্থ্য ও ওষুধ পরিচালনা করুন",
        fam_btn_add: "➕ নতুন সদস্য যুক্ত করুন",
        fam_age_gender: "বয়স ও লিঙ্গ:",
        fam_chronic: "🏥 দীর্ঘস্থায়ী রোগ:",
        fam_allergies: "⚠️ অ্যালার্জি:",
        fam_emergency: "📞 জরুরি নম্বর:",
        fam_btn_current: "✓ বর্তমান প্রোফাইল",
        fam_btn_switch: "👉 এই প্রোফাইলে সুইচ করুন",
        fam_modal_title: "পরিবারের নতুন সদস্য যুক্ত করুন",
        fam_name_label: "সদস্যের নাম",
        fam_name_placeholder: "উদাঃ মোঃ আব্দুল করিম (বাবা)",
        fam_rel_label: "সম্পর্ক",
        fam_rel_father: "বাবা (Father)",
        fam_rel_mother: "মা (Mother)",
        fam_rel_spouse: "স্ত্রী / স্বামী (Spouse)",
        fam_rel_child: "সন্তান (Child)",
        fam_rel_sibling: "ভাই / বোন (Sibling)",
        fam_rel_self: "নিজে (Self)",
        fam_rel_other: "অন্যান্য (Other)",
        fam_blood_label: "রক্তের গ্রুপ",
        fam_age_label: "বয়স (বছর)",
        fam_gender_label: "লিঙ্গ",
        fam_gender_male: "পুরুষ (Male)",
        fam_gender_female: "মহিলা (Female)",
        fam_gender_other: "অন্যান্য",
        fam_chronic_label: "দীর্ঘস্থায়ী রোগ (যদি থাকে)",
        fam_chronic_placeholder: "উদাঃ ডায়াবেটিস, উচ্চ রক্তচাপ, অ্যাজমা",
        fam_allergy_label: "ওষুধের অ্যালার্জি (যদি থাকে)",
        fam_allergy_placeholder: "উদাঃ সালফা ড্রাগ, পেনিসিলিন...",
        fam_contact_label: "জরুরি যোগাযোগ নম্বর",
        fam_btn_submit: "যুক্ত করুন",
        fam_confirm_delete: "আপনি কি এই প্রোফাইলটি মুছে ফেলতে চান?",
        fam_toast_added: "পরিবারের সদস্য যুক্ত হয়েছে!",
        fam_toast_switched: "প্রোফাইল পরিবর্তন করা হয়েছে",
        fam_toast_deleted: "সদস্য মুছে ফেলা হয়েছে",

        // Login & Register
        login_title: "অ্যাকাউন্টে লগইন করুন",
        login_subtitle: "আপনার ও পরিবারের ওষুধ ট্র্যাকিং ড্যাশবোর্ডে প্রবেশ করুন",
        login_demo_banner: "এক ক্লিকে ডেমো টেস্ট করুন:",
        login_demo_user: "👤 সাধারণ ইউজার",
        login_demo_admin: "⚙️ অ্যাডমিন",
        login_email_label: "ইমেইল ঠিকানা",
        login_pass_label: "পাসওয়ার্ড",
        login_btn: "লগইন করুন",
        login_btn_loading: "যাচাই করা হচ্ছে...",
        login_no_acc: "অ্যাকাউন্ট নেই?",
        login_create_acc: "নতুন অ্যাকাউন্ট খুলুন",
        login_toast_success: "সফলভাবে লগইন হয়েছে!",
        reg_title: "নতুন অ্যাকাউন্ট তৈরি করুন",
        reg_subtitle: "আপনার ও পরিবারের নিয়মিত স্বাস্থ্য ট্র্যাকিং শুরু করুন",
        reg_name_label: "পূর্ণ নাম",
        reg_name_placeholder: "উদাঃ মোঃ আরিফুল ইসলাম",
        reg_email_label: "ইমেইল ঠিকানা",
        reg_phone_label: "মোবাইল নম্বর (ঐচ্ছিক)",
        reg_pass_label: "পাসওয়ার্ড",
        reg_pass_placeholder: "কমপক্ষে ৬ অক্ষর",
        reg_btn: "অ্যাকাউন্ট খুলুন",
        reg_btn_loading: "অ্যাকাউন্ট তৈরি হচ্ছে...",
        reg_have_acc: "ইতিমধ্যে অ্যাকাউন্ট আছে?",
        reg_login_link: "লগইন করুন",
        reg_toast_success: "অ্যাকাউন্ট সফলভাবে তৈরি হয়েছে!",

        // Admin
        adm_header_title: "মেডিট্র্যাক অ্যাডমিন কন্ট্রোল প্যানেল",
        adm_header_sub: "সিস্টেম ডেটাবেজ, বাংলাদেশি ফার্মাসিউটিক্যালস ব্র্যান্ড ও বিশেষজ্ঞ ডাক্তার পরিচালনা",
        adm_access_badge: "অ্যাডমিন এক্সেস",
        adm_stat_users: "মোট ইউজার",
        adm_stat_meds: "চলমান ওষুধ",
        adm_stat_doses: "লগ হওয়া ডোজ",
        adm_stat_catalog: "ক্যাটালগ ওষুধ",
        adm_stat_docs: "মোট ডাক্তার",
        adm_med_title: "💊 নতুন বাংলাদেশি ফার্মা ব্র্যান্ড যুক্ত করুন",
        adm_brand_label: "ব্র্যান্ড নাম (Brand Name)",
        adm_brand_placeholder: "উদাঃ Napa Extra, Seclo 20, Monas 10",
        adm_generic_label: "জেনেরিক উপাদান (Generic Name)",
        adm_generic_placeholder: "উদাঃ Paracetamol + Caffeine",
        adm_form_label: "ধরন (Form)",
        adm_strength_label: "মাত্রা (Strength)",
        adm_company_label: "কোম্পানি / প্রস্তুতকারক (Manufacturer)",
        adm_cat_label: "থেরাপিউটিক ক্যাটাগরি",
        adm_btn_add_med: "ক্যাটালগে যুক্ত করুন",
        adm_doc_title: "👨‍⚕️ নতুন বিশেষজ্ঞ ডাক্তার ও চেম্বার যুক্ত করুন",
        adm_doc_name_label: "ডাক্তারের পূর্ণ নাম",
        adm_doc_spec_label: "বিভাগ (Specialty)",
        adm_doc_bmdc_label: "BMDC রেজিঃ নম্বর",
        adm_doc_qual_label: "ডিগ্রী ও পদবী (Qualifications)",
        adm_doc_hosp_label: "হাসপাতাল (Hospital Affiliation)",
        adm_doc_area_label: "এলাকা (Area)",
        adm_doc_cham_label: "চেম্বার ডায়াগনস্টিক",
        adm_doc_phone_label: "সিরিয়াল ফোন নম্বর",
        adm_doc_fee_label: "ভিজিট ফি (৳)",
        adm_btn_add_doc: "ডিরেক্টরিতে ডাক্তার যুক্ত করুন",
        adm_users_title: "নিবন্ধিত ব্যবহারকারী তালিকা",
        adm_th_name: "ইউজার নাম",
        adm_th_email: "ইমেইল",
        adm_th_phone: "মোবাইল",
        adm_th_role: "রোল (Role)",
        adm_th_created: "নিবন্ধন তারিখ"
    },

    en: {
        lang_name: "বাংলা",
        
        // Navigation & Top Bar
        emergency_notice: "🇧🇩 Bangladesh Healthcare & Medication Tracking Platform (MediTrack BD)",
        helpline_health: "Health Helpline: 16263",
        helpline_national: "National Emergency: 999",
        nav_brand_sub: "BD CARE",
        nav_dashboard: "📊 Dashboard",
        nav_medications: "💊 Medications",
        nav_doctors: "👨‍⚕️ Doctors & Chambers",
        nav_appointments: "🗓️ Serials & Visits",
        nav_prescriptions: "📁 Prescriptions",
        nav_family: "👨‍👩‍👧 Family",
        nav_admin: "⚙️ Admin",
        nav_ramadan: "Ramadan Mode",
        nav_ramadan_title: "Adjust medication schedule for Ramadan fasting",
        nav_login: "Login",
        nav_register: "Register",
        nav_logout_title: "Logout",
        
        // Footer
        footer_rights: "© 2026 MediTrack Bangladesh. All rights reserved.",
        footer_disclaimer: "MediTrack is an assistive digital platform for medication adherence and clinical follow-up.",
        footer_feat_bilingual: "🌐 Bilingual Support (Bangla / English)",
        footer_feat_bmdc: "✓ BMDC Verified Data",
        footer_feat_caregiver: "👨‍👩‍👧 Seamless Caregiver Tracking",

        // Landing Page (Index)
        home_badge: "Specialized for Bangladeshi Healthcare & Prescription Culture",
        home_title: "Timely Medication Adherence & Doctor Chamber Tracking Made Simple",
        home_desc: "Eliminate lost paper prescriptions and never forget elderly parents' blood pressure and diabetes doses. 1+0+1 patterns, meal timing rules, and private doctor chamber serials—all in one place.",
        home_btn_demo: "🚀 Try with Demo Account",
        home_btn_register: "Create New Account",
        home_feat_pharma: "✓ Bangladeshi Pharma Brands (Napa, Seclo, Monas)",
        home_feat_caregiver: "✓ Caregiver Tracking for Parents & Family",
        home_feat_chamber: "✓ Top Specialist Chamber & Serial Directory",
        home_card1_icon: "1+0+1",
        home_card1_title: "Bangladeshi Prescription Routines",
        home_card1_desc: "Easily set standard 1+0+1 or 1+1+1 dosing patterns with \"Before Meals\", \"After Meals\", or \"At Bedtime\". Includes automated Ramadan fasting schedule mode.",
        home_card2_icon: "👨‍👩‍👧",
        home_card2_title: "Caregiver Tracking for Parents",
        home_card2_desc: "Working adult children can effortlessly monitor whether elderly parents took their daily blood pressure and diabetes medicines on time from anywhere.",
        home_card3_icon: "🏥",
        home_card3_title: "Private Chambers & Serials",
        home_card3_desc: "Search visiting hours, chamber addresses, and direct booking hotlines for specialists at Popular, Ibn Sina, Labaid, and top medical centers across Bangladesh.",
        home_demo_badge: "⚡ Instant Test Credentials",
        home_demo_title: "Log in with One Click to Test",
        home_demo_desc: "Email: demo@meditrack.bd | Password: password123",
        home_demo_admin: "(Admin Panel: admin@meditrack.bd / admin123)",
        home_demo_btn: "Go to Login Page →",

        // Dashboard
        dash_age_suffix: "yrs",
        dash_add_med: "➕ Add Medication",
        dash_find_doc: "Find Doctors",
        dash_ramadan_notice_title: "Ramadan Fasting Mode Active:",
        dash_ramadan_notice_desc: "Adjust midday doses between Sehri and Iftar as advised by your physician.",
        dash_total_doses: "Today's Total Doses",
        dash_total_sub: "Scheduled for timely intake",
        dash_taken: "Taken Doses",
        dash_taken_sub: "Successfully confirmed doses",
        dash_missed: "Missed Doses",
        dash_missed_sub: "Missed or skipped doses",
        dash_adherence: "7-Day Adherence Rate",
        dash_schedule_title: "🕒 Today's Medication Schedule & Tracking",
        dash_today: "Today",
        dash_loading_meds: "Loading medication schedule...",
        dash_upcoming_serial: "Upcoming Chamber Serial",
        dash_view_all: "View All →",
        dash_serial_label: "Serial:",
        dash_datetime_label: "Date & Time:",
        dash_chamber_call: "📞 Call Chamber Desk",
        dash_no_serial: "Currently no upcoming doctor serials scheduled.",
        dash_book_serial_btn: "Book Chamber Serial",
        dash_chart_title: "7-Day Adherence Trend",
        dash_chart_sub: "Bar Chart",
        dash_helpline_title: "Emergency Medical Helplines",
        dash_shastho: "Shastho Batayan (24/7 Doctors):",
        dash_national: "National Emergency (Ambulance):",
        dash_birdem: "BIRDEM Diabetes Helpline:",
        dash_confirmed_at: "Confirmed at:",
        dash_no_meds: "No active scheduled medicines for this member today.",
        dash_add_first_med: "➕ Add a Medication",
        btn_taken: "✓ Taken",
        btn_missed: "✕ Missed",
        btn_take: "✓ Take",
        btn_miss: "✕ Miss",

        // Slots
        slot_morning_title: "🌅 Morning Doses",
        slot_afternoon_title: "☀️ Afternoon Doses",
        slot_night_title: "🌙 Night & Dinner Doses",
        slot_bedtime_title: "🛌 Bedtime Doses",
        slot_sos_title: "⚡ As Needed (SOS)",
        slot_morning_time: "08:00 AM",
        slot_afternoon_time: "02:00 PM",
        slot_night_time: "09:30 PM",
        slot_bedtime_time: "11:00 PM",
        slot_sos_time: "As Needed",

        // Medications Page
        meds_page_title: "Medication List & Schedule",
        meds_active_member_prefix: "Active Member:",
        meds_btn_add: "➕ Add New Medication",
        meds_section_title: "💊 Active & Ongoing Medications",
        meds_count_suffix: "medications listed",
        meds_chronic_badge: "✓ Chronic / Long-term",
        meds_generic_label: "Generic:",
        meds_prescriber_label: "👨‍⚕️ Prescriber:",
        meds_start_date: "📅 Started:",
        meds_end_date: "End:",
        meds_status_active: "Active",
        meds_status_paused: "Paused",
        meds_delete_tooltip: "Delete",
        meds_empty_text: "No medications added yet.",
        meds_empty_btn: "Add First Medication",
        meds_modal_title: "💊 Add New Medication",
        meds_name_label: "Medicine Name (Search Brand / Generic)",
        meds_name_placeholder: "e.g. Napa Extra, Seclo 20, Monas 10...",
        meds_generic_label_form: "Generic Name (Optional)",
        meds_generic_placeholder: "Paracetamol, Omeprazole...",
        meds_form_label: "Dosage Form",
        meds_form_tablet: "Tablet",
        meds_form_capsule: "Capsule",
        meds_form_syrup: "Syrup",
        meds_form_inhaler: "Inhaler",
        meds_form_drop: "Drop",
        meds_form_injection: "Injection",
        meds_pattern_label: "Prescription Dosage Routine",
        meds_pattern_101: "1+0+1 (Morning & Night)",
        meds_pattern_111: "1+1+1 (Morning, Afternoon & Night)",
        meds_pattern_100: "1+0+0 (Morning only)",
        meds_pattern_010: "0+1+0 (Afternoon only)",
        meds_pattern_001: "0+0+1 (Night only)",
        meds_pattern_1001: "1+0+0+1 (Morning & Bedtime)",
        meds_pattern_sos: "SOS (As Needed)",
        meds_meal_label: "Meal Timing Instruction",
        meds_meal_after: "After Meal",
        meds_meal_before: "20 mins Before Meal",
        meds_meal_empty: "Empty Stomach",
        meds_meal_bedtime: "At Bedtime",
        meds_start_label: "Start Date",
        meds_doctor_label: "Doctor Name",
        meds_doctor_placeholder: "Prescribing Doctor",
        meds_chronic_check: "Chronic Condition Medicine (Daily course)",
        meds_instructions_label: "Special Instructions / Doctor Notes",
        meds_instructions_placeholder: "e.g. Drink plenty of water, avoid sugar...",
        btn_cancel: "Cancel",
        btn_save: "Save",
        meds_confirm_delete: "Are you sure you want to delete this medication?",
        meds_toast_added: "Medication added successfully!",
        meds_toast_status: "Status updated successfully",
        meds_toast_deleted: "Medication deleted successfully",

        // Doctor Directory
        doc_bmdc_badge: "🇧🇩 BMDC Registered Specialist Doctors",
        doc_banner_title: "Bangladesh Specialist Doctor & Chamber Directory",
        doc_banner_sub: "Chamber locations, visiting schedules, and serial phone contacts across Dhaka, Chattogram, and major medical hubs.",
        doc_search_label: "Search Doctor or Chamber",
        doc_search_placeholder: "Doctor name, Popular, Ibn Sina...",
        doc_div_label: "Division",
        doc_div_all: "All Divisions",
        doc_area_label: "Area / Thana",
        doc_area_all: "All Areas",
        doc_spec_label: "Medical Specialty",
        doc_spec_all: "All Specialties",
        doc_spec_med: "Medicine & Diabetes",
        doc_spec_cardio: "Cardiology & Heart",
        doc_spec_neuro: "Neuromedicine",
        doc_spec_pedia: "Pediatrics",
        doc_spec_ortho: "Orthopedics & Bone",
        doc_spec_nephro: "Nephrology & Kidney",
        doc_search_btn: "🔍 Search Directory",
        doc_loading: "Loading doctor directory...",
        doc_not_found: "No doctors found. Please try with different search filters.",
        doc_visiting_time: "Visiting Hours:",
        doc_fee: "Fee:",
        doc_save_serial: "🗓️ Save Chamber Serial",
        doc_call_prefix: "📞 Call",
        doc_modal_title: "🗓️ Add Doctor Chamber Serial",
        doc_patient_name: "Patient Name (Family Member)",
        doc_name_label: "Doctor Name",
        doc_chamber_label: "Chamber & Address",
        doc_date_label: "Appointment Date",
        doc_time_label: "Appointment Time",
        doc_time_placeholder: "06:30 PM",
        doc_serial_no_label: "Serial Number",
        doc_serial_no_placeholder: "e.g. Serial #14",
        doc_hotline_label: "Serial Phone Hotline",
        doc_notes_label: "Advice / Reports to bring",
        doc_notes_placeholder: "e.g. Bring recent FBS and Lipid profile test reports...",
        doc_toast_saved: "Serial and appointment booked successfully!",

        // Appointments
        apt_title: "Doctor Appointments & Chamber Serials",
        apt_patient_prefix: "Patient:",
        apt_subtitle: "Chamber visit & follow-up consultation tracker",
        apt_btn_add: "➕ Add Chamber Serial",
        apt_section_title: "Scheduled & Past Chamber Visits",
        apt_records_count: "Records",
        apt_chamber_label: "Chamber:",
        apt_date_label: "Date:",
        apt_time_label: "Time:",
        apt_hotline_label: "Hotline:",
        apt_advice_label: "Doctor Advice / Notes:",
        apt_followup_label: "🔄 Next Follow-up Consultation:",
        apt_btn_complete: "✓ Completed",
        apt_btn_cancel: "Cancel",
        apt_empty_text: "No chamber serials or appointments scheduled.",
        apt_empty_btn: "Book Serial from Doctor Directory",
        apt_confirm_delete: "Are you sure you want to delete this appointment record?",
        apt_toast_updated: "Appointment updated successfully",
        apt_toast_deleted: "Record deleted successfully",

        // Prescriptions
        rx_title: "Digital Prescription & Lab Report Vault",
        rx_subtitle: "Preserve prescription papers & diagnostic test results digitally",
        rx_print_btn: "🖨️ Print Clinical Summary",
        rx_upload_btn: "📷 Upload Prescription",
        rx_zoom: "🔍 Enlarge Preview",
        rx_view: "View →",
        rx_delete: "Delete",
        rx_empty_text: "No prescriptions or lab reports uploaded yet.",
        rx_empty_btn: "Upload Prescription Image",
        rx_modal_title: "Upload Prescription or Report",
        rx_file_title_label: "Document Title",
        rx_file_title_placeholder: "e.g. BSMMU Prescription / CBC Lab Report",
        rx_doctor_label: "Doctor Name",
        rx_doctor_placeholder: "Prof. Dr. ...",
        rx_hospital_label: "Hospital / Diagnostic Center",
        rx_hospital_placeholder: "e.g. Popular, BIRDEM, DMCH",
        rx_date_label: "Date",
        rx_file_label: "Prescription Image or PDF File",
        rx_diag_label: "Diagnosis Summary or Doctor Advice",
        rx_diag_placeholder: "Brief clinical notes...",
        rx_btn_upload: "Upload Document",
        rx_preview_title: "Prescription Preview",
        rx_confirm_delete: "Are you sure you want to delete this prescription?",
        rx_toast_uploaded: "Prescription uploaded successfully!",
        rx_toast_deleted: "Prescription deleted successfully",

        // Family
        fam_title: "Family & Caregiver Profiles",
        fam_subtitle: "Manage health and medicines for yourself, parents, or family dependents under a single account",
        fam_btn_add: "➕ Add Family Member",
        fam_age_gender: "Age & Gender:",
        fam_chronic: "🏥 Chronic Conditions:",
        fam_allergies: "⚠️ Allergies:",
        fam_emergency: "📞 Emergency Contact:",
        fam_btn_current: "✓ Active Profile",
        fam_btn_switch: "👉 Switch to This Profile",
        fam_modal_title: "Add New Family Member",
        fam_name_label: "Member Name",
        fam_name_placeholder: "e.g. Md. Abdul Karim (Father)",
        fam_rel_label: "Relationship",
        fam_rel_father: "Father",
        fam_rel_mother: "Mother",
        fam_rel_spouse: "Spouse",
        fam_rel_child: "Child",
        fam_rel_sibling: "Sibling",
        fam_rel_self: "Self",
        fam_rel_other: "Other",
        fam_blood_label: "Blood Group",
        fam_age_label: "Age (Years)",
        fam_gender_label: "Gender",
        fam_gender_male: "Male",
        fam_gender_female: "Female",
        fam_gender_other: "Other",
        fam_chronic_label: "Chronic Conditions (if any)",
        fam_chronic_placeholder: "e.g. Diabetes, Hypertension, Asthma",
        fam_allergy_label: "Medicine Allergies (if any)",
        fam_allergy_placeholder: "e.g. Sulfa drugs, Penicillin...",
        fam_contact_label: "Emergency Contact Phone",
        fam_btn_submit: "Add Member",
        fam_confirm_delete: "Are you sure you want to delete this profile?",
        fam_toast_added: "Family member added successfully!",
        fam_toast_switched: "Profile switched successfully",
        fam_toast_deleted: "Member deleted successfully",

        // Login & Register
        login_title: "Log in to Your Account",
        login_subtitle: "Access your family medication and treatment dashboard",
        login_demo_banner: "Test demo with one click:",
        login_demo_user: "👤 General User",
        login_demo_admin: "⚙️ Admin",
        login_email_label: "Email Address",
        login_pass_label: "Password",
        login_btn: "Log In",
        login_btn_loading: "Verifying...",
        login_no_acc: "Don't have an account?",
        login_create_acc: "Create a new account",
        login_toast_success: "Logged in successfully!",
        reg_title: "Create a New Account",
        reg_subtitle: "Start managing healthcare and medication adherence for your family",
        reg_name_label: "Full Name",
        reg_name_placeholder: "e.g. Ariful Islam",
        reg_email_label: "Email Address",
        reg_phone_label: "Mobile Number (Optional)",
        reg_pass_label: "Password",
        reg_pass_placeholder: "At least 6 characters",
        reg_btn: "Register Account",
        reg_btn_loading: "Creating account...",
        reg_have_acc: "Already have an account?",
        reg_login_link: "Log In",
        reg_toast_success: "Account created successfully!",

        // Admin
        adm_header_title: "MediTrack Admin Control Panel",
        adm_header_sub: "Manage system database, Bangladeshi pharmaceutical brands, and specialist doctors",
        adm_access_badge: "Admin Access",
        adm_stat_users: "Total Users",
        adm_stat_meds: "Active Medications",
        adm_stat_doses: "Logged Doses",
        adm_stat_catalog: "Catalog Medicines",
        adm_stat_docs: "Total Doctors",
        adm_med_title: "💊 Add New Bangladeshi Pharma Brand",
        adm_brand_label: "Brand Name",
        adm_brand_placeholder: "e.g. Napa Extra, Seclo 20, Monas 10",
        adm_generic_label: "Generic Name",
        adm_generic_placeholder: "e.g. Paracetamol + Caffeine",
        adm_form_label: "Dosage Form",
        adm_strength_label: "Strength",
        adm_company_label: "Manufacturer Company",
        adm_cat_label: "Therapeutic Category",
        adm_btn_add_med: "Add to Medicine Catalog",
        adm_doc_title: "👨‍⚕️ Add New Specialist Doctor & Chamber",
        adm_doc_name_label: "Doctor's Full Name",
        adm_doc_spec_label: "Medical Specialty",
        adm_doc_bmdc_label: "BMDC Reg. No.",
        adm_doc_qual_label: "Qualifications & Degrees",
        adm_doc_hosp_label: "Hospital Affiliation",
        adm_doc_area_label: "Area / Thana",
        adm_doc_cham_label: "Chamber / Diagnostic Center",
        adm_doc_phone_label: "Serial Phone Hotline",
        adm_doc_fee_label: "Consultation Fee (৳)",
        adm_btn_add_doc: "Add Doctor to Directory",
        adm_users_title: "Registered Users Directory",
        adm_th_name: "Name",
        adm_th_email: "Email",
        adm_th_phone: "Phone",
        adm_th_role: "Role",
        adm_th_created: "Registered On"
    }
};

// Relationship Translation Mapper
const relationshipMap = {
    "Father": { bn: "বাবা", en: "Father" },
    "Mother": { bn: "মা", en: "Mother" },
    "Spouse": { bn: "স্ত্রী / স্বামী", en: "Spouse" },
    "Child": { bn: "সন্তান", en: "Child" },
    "Sibling": { bn: "ভাই / বোন", en: "Sibling" },
    "Self": { bn: "নিজে", en: "Self" },
    "Other": { bn: "অন্যান্য", en: "Other" }
};

function translateRelationship(rel, lang) {
    if (!rel) return "";
    for (const [key, val] of Object.entries(relationshipMap)) {
        if (rel.toLowerCase().includes(key.toLowerCase()) || rel.includes(val.bn)) {
            return val[lang] || rel;
        }
    }
    return rel;
}

// Meal Timing Translation Mapper
function translateMealTiming(val, lang) {
    if (!val) return "";
    const lower = val.toLowerCase();
    if (lower.includes("খাওয়ার পরে") || lower.includes("after meal")) {
        return lang === 'bn' ? "খাওয়ার পরে (After Meal)" : "After Meal";
    }
    if (lower.includes("২০ মিনিট আগে") || lower.includes("before meal")) {
        return lang === 'bn' ? "খাওয়ার ২০ মিনিট আগে (Before Meal)" : "20 mins Before Meal";
    }
    if (lower.includes("খালি পেটে") || lower.includes("empty stomach")) {
        return lang === 'bn' ? "খালি পেটে (Empty Stomach)" : "Empty Stomach";
    }
    if (lower.includes("শোবার আগে") || lower.includes("bedtime")) {
        return lang === 'bn' ? "রাতে শোবার আগে (At Bedtime)" : "At Bedtime";
    }
    return val;
}

// Status Translation Mapper
function translateStatus(status, lang) {
    if (!status) return "";
    const lower = String(status).toLowerCase();
    if (lower === "upcoming" || lower === "আসন্ন") {
        return lang === 'bn' ? "আসন্ন" : "Upcoming";
    }
    if (lower === "completed" || lower === "সম্পন্ন") {
        return lang === 'bn' ? "সম্পন্ন" : "Completed";
    }
    if (lower === "cancelled" || lower === "বাতিল") {
        return lang === 'bn' ? "বাতিল" : "Cancelled";
    }
    if (lower === "true" || lower === "active" || lower === "চলমান") {
        return lang === 'bn' ? "চলমান" : "Active";
    }
    if (lower === "false" || lower === "paused" || lower === "স্থগিত") {
        return lang === 'bn' ? "স্থগিত" : "Paused";
    }
    return status;
}

// Language Helpers
function getLanguage() {
    return localStorage.getItem('meditrack_lang') || 'bn';
}

function setLanguage(lang) {
    localStorage.setItem('meditrack_lang', lang);
    document.cookie = `meditrack_lang=${lang}; path=/; max-age=31536000`;
    applyTranslations();
    window.dispatchEvent(new CustomEvent('languageChanged', { detail: { lang } }));
}

function toggleLanguage() {
    const nextLang = getLanguage() === 'bn' ? 'en' : 'bn';
    setLanguage(nextLang);
    showToast(nextLang === 'bn' ? "বাংলা ভাষা নির্বাচন করা হয়েছে" : "English language selected", "info");
}

function t(key) {
    const lang = getLanguage();
    if (i18n[lang] && i18n[lang][key] !== undefined) {
        return i18n[lang][key];
    }
    return (i18n['bn'] && i18n['bn'][key]) || key;
}

function applyTranslations() {
    const lang = getLanguage();
    const dict = i18n[lang];
    if (!dict) return;

    document.documentElement.lang = lang;

    // Update Language Toggle Button Label
    const langBtnLabel = document.getElementById('lang-btn-label');
    if (langBtnLabel) {
        langBtnLabel.innerText = dict.lang_name;
    }

    // Update Ramadan Mode Button Label
    const ramadanBtn = document.getElementById("ramadan-toggle-btn");
    if (ramadanBtn) {
        const isActive = isRamadanMode();
        if (isActive) {
            ramadanBtn.innerHTML = `<span>🌙</span> <span data-i18n="nav_ramadan">${dict.nav_ramadan}</span> (${lang === 'bn' ? 'সক্রিয়' : 'Active'})`;
        } else {
            ramadanBtn.innerHTML = `<span>🌙</span> <span data-i18n="nav_ramadan">${dict.nav_ramadan}</span>`;
        }
    }

    // Update Elements with data-i18n
    document.querySelectorAll('[data-i18n]').forEach(el => {
        const key = el.getAttribute('data-i18n');
        if (dict[key] !== undefined) {
            el.innerHTML = dict[key];
        }
    });

    // Update Elements with data-i18n-placeholder
    document.querySelectorAll('[data-i18n-placeholder]').forEach(el => {
        const key = el.getAttribute('data-i18n-placeholder');
        if (dict[key] !== undefined) {
            el.placeholder = dict[key];
        }
    });

    // Update Elements with data-i18n-title
    document.querySelectorAll('[data-i18n-title]').forEach(el => {
        const key = el.getAttribute('data-i18n-title');
        if (dict[key] !== undefined) {
            el.title = dict[key];
        }
    });

    // Update Elements with data-relationship
    document.querySelectorAll('[data-relationship]').forEach(el => {
        const rel = el.getAttribute('data-relationship');
        el.innerText = translateRelationship(rel, lang);
    });

    // Update Elements with data-meal-timing
    document.querySelectorAll('[data-meal-timing]').forEach(el => {
        const timing = el.getAttribute('data-meal-timing');
        el.innerText = translateMealTiming(timing, lang);
    });

    // Update Elements with data-status
    document.querySelectorAll('[data-status]').forEach(el => {
        const status = el.getAttribute('data-status');
        el.innerText = translateStatus(status, lang);
    });
}

// Web Audio API Pleasant Medical Notification Chime
function playReminderChime() {
    try {
        const AudioContext = window.AudioContext || window.webkitAudioContext;
        if (!AudioContext) return;
        const ctx = new AudioContext();
        
        const now = ctx.currentTime;
        const osc1 = ctx.createOscillator();
        const osc2 = ctx.createOscillator();
        const gain = ctx.createGain();

        osc1.type = 'sine';
        osc1.frequency.setValueAtTime(587.33, now); // D5
        osc1.frequency.exponentialRampToValueAtTime(880, now + 0.15); // A5

        osc2.type = 'triangle';
        osc2.frequency.setValueAtTime(440, now); // A4
        osc2.frequency.exponentialRampToValueAtTime(659.25, now + 0.15); // E5

        gain.gain.setValueAtTime(0.15, now);
        gain.gain.exponentialRampToValueAtTime(0.001, now + 0.6);

        osc1.connect(gain);
        osc2.connect(gain);
        gain.connect(ctx.destination);

        osc1.start(now);
        osc2.start(now);
        osc1.stop(now + 0.6);
        osc2.stop(now + 0.6);
    } catch (e) {
        console.log("Audio alert not supported or user has not interacted yet.");
    }
}

// Toast Notifications
function showToast(message, type = 'success') {
    const container = document.getElementById('toast-container');
    if (!container) return;

    const toast = document.createElement('div');
    const bgColors = {
        success: 'bg-emerald-600 text-white',
        error: 'bg-rose-600 text-white',
        info: 'bg-teal-600 text-white',
        warning: 'bg-amber-600 text-white'
    };

    toast.className = `flex items-center gap-2 px-4 py-3 rounded-xl shadow-lg font-medium text-sm transition-all transform duration-300 translate-y-2 opacity-0 ${bgColors[type] || bgColors.success}`;
    toast.innerHTML = `
        <svg class="w-5 h-5 flex-shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="${type === 'error' ? 'M6 18L18 6M6 6l12 12' : 'M5 13l4 4L19 7'}"></path>
        </svg>
        <span>${message}</span>
    `;

    container.appendChild(toast);
    setTimeout(() => {
        toast.classList.remove('translate-y-2', 'opacity-0');
    }, 10);

    setTimeout(() => {
        toast.classList.add('opacity-0', 'translate-y-2');
        setTimeout(() => toast.remove(), 300);
    }, 3500);
}

// Active Profile Management
function getActiveMemberId() {
    return localStorage.getItem('meditrack_active_member_id') || null;
}

function setActiveMemberId(id) {
    localStorage.setItem('meditrack_active_member_id', id);
    window.location.reload();
}

// Ramadan Fasting Mode Management
function toggleRamadanMode() {
    const current = localStorage.getItem('meditrack_ramadan_mode') === 'true';
    const next = !current;
    localStorage.setItem('meditrack_ramadan_mode', next ? 'true' : 'false');
    
    if (next) {
        showToast(getLanguage() === 'bn' ? "রোজার সময়সূচী সক্রিয় করা হয়েছে (রমজান মোড)" : "Ramadan fasting schedule activated", "info");
    } else {
        showToast(getLanguage() === 'bn' ? "স্বাভাবিক সময়সূচী সক্রিয় করা হয়েছে" : "Standard schedule activated", "info");
    }
    setTimeout(() => window.location.reload(), 600);
}

function isRamadanMode() {
    return localStorage.getItem('meditrack_ramadan_mode') === 'true';
}

document.addEventListener("DOMContentLoaded", () => {
    // Initial Translations
    applyTranslations();

    // Sync Ramadan UI Button
    const ramadanBtn = document.getElementById("ramadan-toggle-btn");
    if (ramadanBtn) {
        if (isRamadanMode()) {
            ramadanBtn.classList.remove("bg-slate-100", "text-slate-600");
            ramadanBtn.classList.add("bg-amber-100", "text-amber-800", "border-amber-300");
            ramadanBtn.innerHTML = `🌙 <span data-i18n="nav_ramadan">${t('nav_ramadan')}</span> (${getLanguage() === 'bn' ? 'সক্রিয়' : 'Active'})`;
        }
    }

    // Auto-populate Member Selectors
    const memberSelect = document.getElementById("active-member-select");
    if (memberSelect) {
        const activeId = getActiveMemberId();
        if (activeId) {
            memberSelect.value = activeId;
        }
        memberSelect.addEventListener("change", (e) => {
            setActiveMemberId(e.target.value);
        });
    }
});
