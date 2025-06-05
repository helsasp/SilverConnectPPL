# utils.py
# Helper functions dan utilities untuk SilverConnect

import time
import random
import json
from typing import Dict, List, Any, Optional
from config import UIElements

class InputValidator:
    """Validator untuk input user yang aman dan ramah senior"""
    
    @staticmethod
    def validate_username(username: str) -> tuple[bool, str]:
        """Validasi username dengan aturan yang jelas"""
        if not username:
            return False, "Username tidak boleh kosong"
        
        if len(username) < 3:
            return False, "Username minimal 3 karakter"
        
        if len(username) > 20:
            return False, "Username maksimal 20 karakter"
        
        if not username.replace('_', '').replace('-', '').isalnum():
            return False, "Username hanya boleh huruf, angka, underscore, dan dash"
        
        # Check for inappropriate patterns
        inappropriate = ['admin', 'root', 'test', '123456']
        if username.lower() in inappropriate:
            return False, "Username ini sudah umum digunakan, silakan pilih yang lain"
        
        return True, "Username valid"
    
    @staticmethod
    def validate_full_name(name: str) -> tuple[bool, str]:
        """Validasi nama lengkap"""
        if not name or not name.strip():
            return False, "Nama lengkap tidak boleh kosong"
        
        cleaned_name = name.strip()
        if len(cleaned_name) < 2:
            return False, "Nama terlalu pendek"
        
        if len(cleaned_name) > 50:
            return False, "Nama terlalu panjang (maksimal 50 karakter)"
        
        # Check for valid characters (letters, spaces, common punctuation)
        valid_chars = set("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ .',-")
        if not all(c in valid_chars for c in cleaned_name):
            return False, "Nama hanya boleh berisi huruf, spasi, dan tanda baca umum"
        
        return True, cleaned_name
    
    @staticmethod
    def validate_age(age_str: str) -> tuple[bool, int]:
        """Validasi usia dengan range yang masuk akal untuk senior"""
        if not age_str or not age_str.strip():
            return False, 65  # Default age
        
        try:
            age = int(age_str.strip())
            if age < 40:
                return False, 40  # Minimum for senior-focused platform
            if age > 120:
                return False, 99  # Reasonable maximum
            return True, age
        except ValueError:
            return False, 65  # Default age if invalid input
    
    @staticmethod
    def validate_choice(choice: str, max_options: int) -> tuple[bool, int]:
        """Validasi pilihan numerik dengan error handling yang baik"""
        if not choice or not choice.strip():
            return False, 0
        
        try:
            choice_num = int(choice.strip())
            if 1 <= choice_num <= max_options:
                return True, choice_num
            return False, 0
        except ValueError:
            return False, 0
    
    @staticmethod
    def validate_multiple_choice(choices_str: str, max_options: int) -> tuple[bool, List[int]]:
        """Validasi pilihan ganda dengan error handling yang comprehensive"""
        if not choices_str or not choices_str.strip():
            return False, []
        
        try:
            # Clean input and split by comma
            cleaned_input = choices_str.strip().replace(' ', '')
            choice_parts = [part.strip() for part in cleaned_input.split(",") if part.strip()]
            
            if not choice_parts:
                return False, []
            
            # Convert to integers and validate
            choices = []
            for part in choice_parts:
                choice_num = int(part)
                if 1 <= choice_num <= max_options:
                    if choice_num not in choices:  # Avoid duplicates
                        choices.append(choice_num)
                else:
                    return False, []  # Invalid choice found
            
            if choices:
                return True, sorted(choices)  # Return sorted list
            return False, []
            
        except ValueError:
            return False, []
    
    @staticmethod
    def validate_time_preference(time_input: str) -> tuple[bool, str]:
        """Validasi preferensi waktu"""
        if not time_input or not time_input.strip():
            return True, "pagi"  # Default
        
        time_input = time_input.strip().lower()
        valid_times = {
            '1': 'pagi', 'pagi': 'pagi', 'morning': 'pagi',
            '2': 'siang', 'siang': 'siang', 'afternoon': 'siang', 
            '3': 'sore', 'sore': 'sore', 'evening': 'sore'
        }
        
        return True, valid_times.get(time_input, 'pagi')
    
    @staticmethod
    def sanitize_text_input(text: str) -> str:
        """Sanitize text input untuk keamanan"""
        if not text:
            return ""
        
        # Remove potential harmful characters
        sanitized = text.strip()
        
        # Remove excessive whitespace
        sanitized = ' '.join(sanitized.split())
        
        # Basic length limit
        if len(sanitized) > 500:
            sanitized = sanitized[:500]
        
        return sanitized

class UIHelper:
    """Helper untuk UI dan formatting yang konsisten"""
    
    def __init__(self):
        self.ui = UIElements()
    
    def print_header(self, title: str, subtitle: str = "", use_emoji: bool = True):
        """Print header yang konsisten dengan styling yang lebih baik"""
        print(f"\n{self.ui.SECTION_SEPARATOR}")
        if use_emoji:
            print(f"{self.ui.SPARKLE} {title.upper()} {self.ui.SPARKLE}")
        else:
            print(f" {title.upper()} ")
        print(f"{self.ui.SECTION_SEPARATOR}")
        
        if subtitle:
            print(f"{subtitle}")
            print()
    
    def print_step_header(self, step_num: int, title: str, description: str = ""):
        """Print header untuk langkah-langkah yang berurutan"""
        print(f"\n{self.ui.STAR} LANGKAH {step_num}: {title.upper()}")
        print("━" * 50)
        if description:
            print(f"{description}")
            print()
    
    def print_subsection(self, title: str):
        """Print subsection yang konsisten"""
        print(f"\n{self.ui.SUBSECTION_SEPARATOR}")
        print(f"{self.ui.STAR} {title}")
        print(f"{self.ui.SUBSECTION_SEPARATOR}")
    
    def print_success(self, message: str, icon: str = None):
        """Print pesan sukses yang konsisten"""
        success_icon = icon or self.ui.SUCCESS
        print(f"{success_icon} {message}")
    
    def print_error(self, message: str, suggestion: str = "", icon: str = None):
        """Print pesan error yang membantu"""
        error_icon = icon or self.ui.ERROR
        print(f"{error_icon} {message}")
        if suggestion:
            print(f"{self.ui.INFO} {suggestion}")
    
    def print_warning(self, message: str, icon: str = None):
        """Print pesan warning yang konsisten"""
        warning_icon = icon or self.ui.WARNING
        print(f"{warning_icon} {message}")
    
    def print_info(self, message: str, icon: str = None):
        """Print pesan info yang konsisten"""
        info_icon = icon or self.ui.INFO
        print(f"{info_icon} {message}")
    
    def print_list_with_icons(self, items: List[Dict], title: str = "", show_numbers: bool = True):
        """Print list dengan icon yang sesuai dan numbering"""
        if title:
            print(f"\n{self.ui.SPARKLE} {title}:")
        
        for i, item in enumerate(items, 1):
            icon = item.get('icon', self.ui.STAR)
            name = item.get('name', f'Item {i}')
            description = item.get('description', '')
            
            if show_numbers:
                print(f"[{i}] {icon} {name}")
            else:
                print(f"  {icon} {name}")
            
            if description:
                print(f"    {description}")
    
    def print_two_column_list(self, items: List[tuple], title: str = ""):
        """Print list dalam 2 kolom untuk readability yang lebih baik"""
        if title:
            print(f"\n{self.ui.SPARKLE} {title}:")
            print()
        
        for i in range(0, len(items), 2):
            left_item = items[i]
            left_text = f"[{i+1:2d}] {left_item[1] if len(left_item) > 1 else ''} {left_item[0]:<20}"
            
            if i+1 < len(items):
                right_item = items[i+1]
                right_text = f"[{i+2:2d}] {right_item[1] if len(right_item) > 1 else ''} {right_item[0]}"
                print(f"{left_text} {right_text}")
            else:
                print(left_text)
    
    def get_user_choice(self, prompt: str, max_choice: int, allow_quit: bool = True, 
                       validator_func=None) -> Optional[int]:
        """Dapatkan pilihan user dengan validasi yang lebih baik"""
        while True:
            quit_text = " atau 'q' untuk keluar" if allow_quit else ""
            choice = input(f"{self.ui.SELECT} {prompt} (1-{max_choice}{quit_text}): ").strip()
            
            if allow_quit and choice.lower() == 'q':
                return None
            
            # Use custom validator if provided
            if validator_func:
                is_valid, validated_choice = validator_func(choice, max_choice)
            else:
                is_valid, validated_choice = InputValidator.validate_choice(choice, max_choice)
            
            if is_valid:
                return validated_choice
            else:
                self.print_warning(f"Pilihan '{choice}' tidak valid. Silakan masukkan angka 1-{max_choice}")
                if allow_quit:
                    print(f"  💡 Tip: Ketik 'q' jika ingin keluar")
    
    def get_multiple_choice(self, prompt: str, max_choice: int, min_selections: int = 1) -> List[int]:
        """Dapatkan multiple choice dengan validation yang baik"""
        while True:
            print(f"\n💡 Tip: Pisahkan pilihan dengan koma (contoh: 1,3,5)")
            if min_selections > 1:
                print(f"     Pilih minimal {min_selections} item")
            
            choices_input = input(f"{self.ui.SELECT} {prompt}: ").strip()
            
            if not choices_input:
                self.print_warning("Silakan masukkan pilihan Anda")
                continue
            
            is_valid, choices = InputValidator.validate_multiple_choice(choices_input, max_choice)
            
            if is_valid and len(choices) >= min_selections:
                return choices
            elif is_valid and len(choices) < min_selections:
                self.print_warning(f"Pilih minimal {min_selections} item")
            else:
                self.print_warning(f"Format tidak valid. Gunakan angka 1-{max_choice} dipisah koma")
                print(f"  Contoh yang benar: 1,3,5")
    
    def get_yes_no_choice(self, prompt: str, default: bool = True, show_explanation: bool = False) -> bool:
        """Dapatkan pilihan ya/tidak dengan UX yang lebih baik"""
        default_text = "(Y/n)" if default else "(y/N)"
        
        if show_explanation:
            print(f"  💡 Y = Ya/Yes, N = Tidak/No, Enter = default")
        
        while True:
            choice = input(f"{prompt} {default_text}: ").strip().lower()
            
            if not choice:
                return default
            
            if choice in ['y', 'yes', 'ya', '1']:
                return True
            elif choice in ['n', 'no', 'tidak', '0']:
                return False
            else:
                self.print_warning("Ketik 'y' untuk ya atau 'n' untuk tidak")
    
    def get_text_input(self, prompt: str, required: bool = True, max_length: int = 100, 
                      validator_func=None) -> str:
        """Dapatkan text input dengan validation"""
        while True:
            text = input(f"{prompt}: ").strip()
            
            if not text and required:
                self.print_warning("Input tidak boleh kosong")
                continue
            
            if not text and not required:
                return ""
            
            if len(text) > max_length:
                self.print_warning(f"Input terlalu panjang (maksimal {max_length} karakter)")
                continue
            
            # Use custom validator if provided
            if validator_func:
                is_valid, result = validator_func(text)
                if is_valid:
                    return result
                else:
                    self.print_warning(f"Input tidak valid: {result}")
                    continue
            
            # Default sanitization
            sanitized_text = InputValidator.sanitize_text_input(text)
            return sanitized_text
    
    def print_progress_bar(self, current: int, total: int, width: int = 30, show_percentage: bool = True):
        """Print progress bar yang lebih informatif"""
        if total == 0:
            return
        
        progress = current / total
        filled_width = int(width * progress)
        
        bar = "█" * filled_width + "░" * (width - filled_width)
        
        if show_percentage:
            percentage = int(progress * 100)
            print(f"{self.ui.STATS} Progress: [{bar}] {percentage}% ({current}/{total})")
        else:
            print(f"{self.ui.STATS} Progress: [{bar}] ({current}/{total})")
    
    def print_confirmation_summary(self, items: List[str], title: str = "Ringkasan Pilihan Anda"):
        """Print ringkasan untuk konfirmasi user"""
        print(f"\n{self.ui.SUMMARY} {title}:")
        for i, item in enumerate(items, 1):
            print(f"  {i}. {item}")
        print()
    
    def print_loading_animation(self, message: str, duration: float = 2.0):
        """Print animasi loading sederhana"""
        import time
        import sys
        
        animation = [
            f"{self.ui.PENDING} {message}",
            f"⏳ {message}.",
            f"⏳ {message}..",
            f"⏳ {message}...",
            f"{self.ui.SUCCESS} {message} selesai!"
        ]
        
        step_duration = duration / len(animation)
        
        for frame in animation:
            sys.stdout.write(f"\r{frame}")
            sys.stdout.flush()
            time.sleep(step_duration)
        
        print()  # New line after animation

class DataManager:
    """Manager untuk save/load data (untuk mode persistent di masa depan)"""
    
    @staticmethod
    def save_user_session(username: str, data: Dict) -> bool:
        """Simpan session user (placeholder untuk future development)"""
        try:
            # Untuk sekarang hanya print, nanti bisa implement ke file/database
            print(f"[DataManager] Session data saved for {username}")
            return True
        except Exception as e:
            print(f"[DataManager] Error saving session: {e}")
            return False
    
    @staticmethod
    def load_user_session(username: str) -> Optional[Dict]:
        """Load session user (placeholder untuk future development)"""
        try:
            # Placeholder - return None untuk sekarang
            return None
        except Exception as e:
            print(f"[DataManager] Error loading session: {e}")
            return None
    
    @staticmethod
    def export_user_data(username: str, data: Dict) -> str:
        """Export data user ke format yang bisa dibaca"""
        try:
            timestamp = time.strftime("%Y%m%d_%H%M%S")
            
            export_data = {
                "user": username,
                "export_time": timestamp,
                "profile": data.get("user_data", {}),
                "communities": data.get("communities", []),
                "activities": data.get("activities", [])
            }
            
            # Convert ke JSON format yang readable
            json_str = json.dumps(export_data, indent=2, ensure_ascii=False)
            
            return json_str
        except Exception as e:
            return f"Error exporting data: {e}"

class RecommendationEngine:
    """Engine untuk memberikan rekomendasi yang smart"""
    
    def __init__(self):
        self.ui = UIElements()
    
    def get_smart_recommendations(self, user_data: Dict, available_items: List[Dict], 
                                item_type: str = "activity") -> List[Dict]:
        """Algoritma rekomendasi yang lebih cerdas dengan data yang diperkaya"""
        
        if not user_data or not available_items:
            return []
        
        user_interests = user_data.get('interests', [])
        user_age = user_data.get('age', 65)
        activity_level = user_data.get('activity_level', 'sedang')
        preferences = user_data.get('preferences', {})
        
        recommendations = []
        
        for item in available_items:
            score = self._calculate_recommendation_score(
                item, user_interests, user_age, activity_level, preferences, item_type
            )
            
            if score > 0.2:  # Lower threshold untuk lebih banyak rekomendasi
                reasons = self._get_recommendation_reasons(item, user_data, item_type)
                recommendations.append({
                    'item': item,
                    'score': score,
                    'reasons': reasons,
                    'match_percentage': int(score * 100)
                })
        
        # Sort by score descending
        recommendations.sort(key=lambda x: x['score'], reverse=True)
        
        return recommendations[:8]  # Top 8 recommendations
    
    def _calculate_recommendation_score(self, item: Dict, interests: List[str], 
                                     age: int, activity_level: str, 
                                     preferences: Dict, item_type: str) -> float:
        """Hitung score rekomendasi dengan algoritma yang lebih sophisticated"""
        
        score = 0.0
        
        # Interest matching (45% weight) - increased importance
        interest_score = self._calculate_interest_match(item, interests, item_type)
        score += interest_score * 0.45
        
        # Age appropriateness (20% weight)
        age_score = self._calculate_age_appropriateness(item, age, item_type)
        score += age_score * 0.20
        
        # Activity level matching (20% weight)
        activity_score = self._calculate_activity_level_match(item, activity_level, item_type)
        score += activity_score * 0.20
        
        # Time preference (10% weight)
        time_score = self._calculate_time_preference_match(item, preferences, item_type)
        score += time_score * 0.10
        
        # Social preference (5% weight)
        social_score = self._calculate_social_preference_match(item, preferences, item_type)
        score += social_score * 0.05
        
        return min(score, 1.0)
    
    def _calculate_interest_match(self, item: Dict, interests: List[str], item_type: str) -> float:
        """Hitung kecocokan dengan minat user - lebih komprehensif"""
        if not interests:
            return 0.3  # Default score
        
        item_category = item.get('category', '').lower()
        item_name = item.get('name', '').lower()
        
        # Enhanced mapping dengan sinonim dan related terms
        interest_category_map = {
            'berkebun': ['hobi', 'hobby', 'nature', 'gardening'],
            'berkebun vertikal': ['hobi', 'hobby', 'nature', 'gardening'],
            'memasak': ['hobi', 'hobby', 'cooking', 'kuliner'],
            'memasak kue': ['hobi', 'hobby', 'cooking', 'baking'],
            'membaca': ['edukasi', 'education', 'literature', 'intelektual'],
            'jalan kaki': ['olahraga', 'fitness', 'outdoor', 'walking'],
            'yoga': ['olahraga', 'fitness', 'kesehatan', 'wellness', 'mindfulness'],
            'olahraga ringan': ['olahraga', 'fitness', 'exercise'],
            'seni': ['kreatif', 'creative', 'art', 'artistic'],
            'musik': ['kreatif', 'creative', 'entertainment', 'art'],
            'fotografi': ['kreatif', 'creative', 'art', 'hobby'],
            'menulis': ['kreatif', 'creative', 'literature', 'edukasi'],
            'crafting': ['kreatif', 'creative', 'hobby', 'art'],
            'teknologi': ['edukasi', 'education', 'modern', 'digital'],
            'travelling': ['hobby', 'adventure', 'exploration'],
            'bahasa asing': ['edukasi', 'education', 'communication'],
            'bermain kartu': ['entertainment', 'social', 'strategy'],
            'catur': ['strategy', 'intellectual', 'competitive'],
            'berkumpul dengan keluarga': ['social', 'family', 'community'],
            'menonton film': ['entertainment', 'relaxation', 'culture']
        }
        
        # Name-based matching untuk aktivitas spesifik
        interest_name_map = {
            'berkebun': ['garden', 'plant', 'tanam', 'berkebun', 'hidroponik'],
            'memasak': ['masak', 'cook', 'kuliner', 'resep', 'chef'],
            'yoga': ['yoga', 'meditation', 'meditasi', 'mindfulness'],
            'jalan kaki': ['jalan', 'walk', 'walking', 'trekking'],
            'seni': ['seni', 'art', 'lukis', 'paint', 'creative'],
            'teknologi': ['digital', 'tech', 'smartphone', 'internet', 'komputer']
        }
        
        match_score = 0.0
        max_possible_score = 0.0
        
        for interest in interests:
            interest_lower = interest.lower()
            max_possible_score += 1.0
            
            # Check category match
            if interest_lower in interest_category_map:
                relevant_categories = interest_category_map[interest_lower]
                if item_category in relevant_categories:
                    match_score += 0.8
                    continue
            
            # Check name match
            if interest_lower in interest_name_map:
                relevant_names = interest_name_map[interest_lower]
                if any(name in item_name for name in relevant_names):
                    match_score += 0.9
                    continue
            
            # Partial match untuk kategori umum
            if interest_lower in item_category or item_category in interest_lower:
                match_score += 0.6
            elif any(word in item_name for word in interest_lower.split()):
                match_score += 0.5
        
        # Normalize score
        if max_possible_score > 0:
            normalized_score = match_score / max_possible_score
            return min(normalized_score, 1.0)
        
        return 0.3  # Default
    
    def _get_recommendation_reasons(self, item: Dict, user_data: Dict, item_type: str) -> List[str]:
        """Dapatkan alasan mengapa item ini direkomendasikan - lebih spesifik"""
        reasons = []
        
        interests = user_data.get('interests', [])
        activity_level = user_data.get('activity_level', 'sedang')
        age = user_data.get('age', 65)
        preferences = user_data.get('preferences', {})
        
        item_category = item.get('category', '').lower()
        item_name = item.get('name', '').lower()
        
        # Interest-based reasons - lebih spesifik
        interest_matches = []
        for interest in interests:
            interest_lower = interest.lower()
            
            # Specific matching logic
            if interest_lower in ['berkebun', 'berkebun vertikal'] and ('garden' in item_name or item_category == 'hobi'):
                interest_matches.append(f"Sesuai dengan minat {interest} Anda")
            elif interest_lower in ['memasak', 'memasak kue'] and ('masak' in item_name or 'cook' in item_name):
                interest_matches.append(f"Perfect untuk hobi {interest} Anda")
            elif interest_lower == 'yoga' and 'yoga' in item_name:
                interest_matches.append(f"Ideal untuk praktik {interest} Anda")
            elif interest_lower == 'teknologi' and ('digital' in item_name or 'tech' in item_name):
                interest_matches.append(f"Cocok untuk interest {interest} Anda")
            elif interest_lower in ['jalan kaki', 'olahraga ringan'] and item_category == 'olahraga':
                interest_matches.append(f"Mendukung aktivitas {interest} Anda")
            elif interest_lower in ['seni', 'crafting'] and item_category in ['kreatif', 'creative']:
                interest_matches.append(f"Mengembangkan bakat {interest} Anda")
        
        reasons.extend(interest_matches[:2])  # Max 2 interest reasons
        
        # Activity level reasons
        if item_type == "activity":
            difficulty = item.get('difficulty', 'sedang')
            if activity_level == difficulty:
                reasons.append(f"Level {difficulty} sesuai dengan preferensi Anda")
            elif activity_level == 'ringan' and difficulty == 'mudah':
                reasons.append("Aktivitas yang tidak terlalu berat")
        
        # Age-specific reasons
        if age >= 70:
            if item_type == "activity" and item.get('difficulty') == 'mudah':
                reasons.append("Aman dan comfortable untuk usia Anda")
        elif age >= 60:
            if item_category in ['kesehatan', 'wellness']:
                reasons.append("Baik untuk menjaga kesehatan di usia Anda")
        
        # Social preference reasons
        if item_type == "community":
            members = item.get('members', 0)
            if members >= 20:
                reasons.append("Komunitas yang aktif dengan banyak anggota")
            elif 10 <= members < 20:
                reasons.append("Ukuran komunitas yang ideal untuk interaksi")
        elif item_type == "activity":
            participants = item.get('participants', 0)
            max_participants = item.get('max_participants', 20)
            if participants / max_participants < 0.7:
                reasons.append("Masih banyak tempat tersedia")
        
        # Time preference reasons
        preferred_time = preferences.get('preferred_time', '')
        if item_type == "activity" and preferred_time:
            item_time = item.get('time', '')
            time_mapping = {
                'pagi': ['06:', '07:', '08:', '09:'],
                'siang': ['10:', '11:', '12:', '13:', '14:'],
                'sore': ['15:', '16:', '17:', '18:']
            }
            
            if preferred_time in time_mapping:
                if any(time_prefix in item_time for time_prefix in time_mapping[preferred_time]):
                    reasons.append(f"Jadwal {preferred_time} sesuai preferensi Anda")
        
        # Price-based reasons for activities
        if item_type == "activity":
            price = item.get('price', 'Gratis')
            if price == 'Gratis':
                reasons.append("Gratis - tidak ada biaya tambahan")
            elif 'Rp' in price:
                try:
                    # Extract numeric value
                    price_num = int(''.join(filter(str.isdigit, price)))
                    if price_num <= 50000:
                        reasons.append("Harga terjangkau")
                except:
                    pass
        
        # Quality indicators
        if item_type == "activity":
            instructor = item.get('instructor', '')
            if instructor and instructor != 'TBA':
                reasons.append(f"Dipandu oleh {instructor} yang berpengalaman")
        
        # Default reason if none found
        if not reasons:
            reasons.append("Rekomendasi berdasarkan profil Anda")
        
        return reasons[:3]  # Maksimal 3 alasan untuk readability
    
    def _calculate_recommendation_score(self, item: Dict, interests: List[str], 
                                     age: int, activity_level: str, 
                                     preferences: Dict, item_type: str) -> float:
        """Hitung score rekomendasi dengan algoritma yang lebih sophisticated"""
        
        score = 0.0
        
        # Interest matching (40% weight)
        interest_score = self._calculate_interest_match(item, interests, item_type)
        score += interest_score * 0.4
        
        # Age appropriateness (25% weight)
        age_score = self._calculate_age_appropriateness(item, age, item_type)
        score += age_score * 0.25
        
        # Activity level matching (20% weight)
        activity_score = self._calculate_activity_level_match(item, activity_level, item_type)
        score += activity_score * 0.2
        
        # Time preference (10% weight)
        time_score = self._calculate_time_preference_match(item, preferences, item_type)
        score += time_score * 0.1
        
        # Social preference (5% weight)
        social_score = self._calculate_social_preference_match(item, preferences, item_type)
        score += social_score * 0.05
        
        return min(score, 1.0)
    
    def _calculate_interest_match(self, item: Dict, interests: List[str], item_type: str) -> float:
        """Hitung kecocokan dengan minat user"""
        if not interests:
            return 0.3  # Default score
        
        item_categories = []
        if item_type == "activity":
            item_categories = [item.get('category', '').lower()]
        elif item_type == "community":
            item_categories = [item.get('category', '').lower()]
        
        # Mapping interests to categories
        interest_category_map = {
            'berkebun': ['hobi', 'hobby'],
            'memasak': ['hobi', 'hobby'],
            'membaca': ['edukasi', 'education'],
            'jalan kaki': ['olahraga', 'fitness'],
            'yoga': ['olahraga', 'fitness', 'kesehatan'],
            'seni': ['kreatif', 'creative'],
            'musik': ['kreatif', 'creative'],
            'olahraga': ['olahraga', 'fitness']
        }
        
        match_score = 0.0
        for interest in interests:
            interest_lower = interest.lower()
            if interest_lower in interest_category_map:
                relevant_categories = interest_category_map[interest_lower]
                for category in item_categories:
                    if category in relevant_categories:
                        match_score += 0.8 / len(interests)  # Weighted by number of interests
        
        return min(match_score, 1.0)
    
    def _calculate_age_appropriateness(self, item: Dict, age: int, item_type: str) -> float:
        """Hitung kesesuaian dengan usia"""
        # Semua item diasumsikan sesuai untuk senior, tapi ada gradasi
        if age >= 80:
            # Prioritaskan aktivitas yang lebih ringan
            if item_type == "activity":
                difficulty = item.get('difficulty', 'sedang').lower()
                if difficulty == 'mudah':
                    return 1.0
                elif difficulty == 'sedang':
                    return 0.7
                else:
                    return 0.3
        elif age >= 65:
            # Balanced approach
            return 0.8
        else:
            # Younger seniors bisa lebih aktif
            return 0.9
        
        return 0.8  # Default
    
    def _calculate_activity_level_match(self, item: Dict, activity_level: str, item_type: str) -> float:
        """Hitung kecocokan level aktivitas"""
        if item_type != "activity":
            return 0.8  # Default untuk non-activity items
        
        item_difficulty = item.get('difficulty', 'sedang').lower()
        
        level_mapping = {
            'ringan': {'mudah': 1.0, 'sedang': 0.5, 'sulit': 0.1},
            'sedang': {'mudah': 0.7, 'sedang': 1.0, 'sulit': 0.6},
            'aktif': {'mudah': 0.4, 'sedang': 0.8, 'sulit': 1.0}
        }
        
        return level_mapping.get(activity_level, {}).get(item_difficulty, 0.5)
    
    def _calculate_time_preference_match(self, item: Dict, preferences: Dict, item_type: str) -> float:
        """Hitung kecocokan preferensi waktu"""
        if item_type != "activity":
            return 0.8  # Default untuk non-activity items
        
        preferred_time = preferences.get('preferred_time', 'pagi')
        item_time = item.get('time', '10:00')
        
        try:
            item_hour = int(item_time.split(':')[0])
            
            time_ranges = {
                'pagi': (6, 11),
                'siang': (11, 15),
                'sore': (15, 19)
            }
            
            start, end = time_ranges.get(preferred_time, (6, 11))
            
            if start <= item_hour < end:
                return 1.0
            else:
                return 0.3
                
        except (ValueError, IndexError):
            return 0.5  # Default jika parsing gagal
    
    def _calculate_social_preference_match(self, item: Dict, preferences: Dict, item_type: str) -> float:
        """Hitung kecocokan preferensi sosial"""
        prefers_group = preferences.get('prefers_group_activities', True)
        
        if item_type == "activity":
            participants = item.get('participants', 1)
            if prefers_group:
                return 1.0 if participants >= 5 else 0.5
            else:
                return 1.0 if participants <= 5 else 0.7
        elif item_type == "community":
            members = item.get('members', 1)
            if prefers_group:
                return 1.0 if members >= 10 else 0.6
            else:
                return 1.0 if members <= 15 else 0.8
        
        return 0.8  # Default
    
    def _get_recommendation_reasons(self, item: Dict, user_data: Dict, item_type: str) -> List[str]:
        """Dapatkan alasan mengapa item ini direkomendasikan"""
        reasons = []
        
        interests = user_data.get('interests', [])
        activity_level = user_data.get('activity_level', 'sedang')
        
        # Interest-based reasons
        item_category = item.get('category', '').lower()
        for interest in interests:
            if interest.lower() in ['berkebun', 'memasak'] and item_category in ['hobi', 'hobby']:
                reasons.append(f"Sesuai dengan minat {interest} Anda")
            elif interest.lower() in ['jalan kaki', 'yoga', 'olahraga'] and item_category in ['olahraga', 'fitness']:
                reasons.append(f"Cocok untuk minat {interest} Anda")
        
        # Activity level reasons
        if item_type == "activity":
            difficulty = item.get('difficulty', 'sedang')
            if activity_level == difficulty:
                reasons.append(f"Sesuai dengan level aktivitas {activity_level} Anda")
        
        # Social reasons
        if item_type == "community":
            members = item.get('members', 0)
            if members >= 10:
                reasons.append("Komunitas yang aktif dengan banyak anggota")
        
        # Default reason if none found
        if not reasons:
            reasons.append("Rekomendasi berdasarkan profil Anda")
        
        return reasons[:3]  # Maksimal 3 alasan

class AnalyticsHelper:
    """Helper untuk analytics dan statistik penggunaan"""
    
    def __init__(self):
        self.ui = UIElements()
    
    def calculate_engagement_metrics(self, user_data: Dict, communities: List[Dict], 
                                   activities: List[Dict]) -> Dict:
        """Hitung metrik engagement user"""
        
        metrics = {
            'profile_completion': self._calculate_profile_completion(user_data),
            'social_engagement': self._calculate_social_engagement(communities),
            'activity_participation': self._calculate_activity_participation(activities),
            'overall_engagement': 0
        }
        
        # Calculate overall engagement
        metrics['overall_engagement'] = (
            metrics['profile_completion'] * 0.3 +
            metrics['social_engagement'] * 0.4 +
            metrics['activity_participation'] * 0.3
        )
        
        return metrics
    
    def _calculate_profile_completion(self, user_data: Dict) -> float:
        """Hitung tingkat kelengkapan profil"""
        required_fields = ['full_name', 'age', 'interests', 'activity_level']
        completed = sum(1 for field in required_fields if user_data.get(field))
        return completed / len(required_fields)
    
    def _calculate_social_engagement(self, communities: List[Dict]) -> float:
        """Hitung tingkat engagement sosial"""
        if not communities:
            return 0.0
        
        # Simulasi berdasarkan jumlah komunitas dan aktivitas
        base_score = min(len(communities) / 3, 1.0)  # Optimal 3 komunitas
        return base_score
    
    def _calculate_activity_participation(self, activities: List[Dict]) -> float:
        """Hitung tingkat partisipasi aktivitas"""
        if not activities:
            return 0.0
        
        # Simulasi berdasarkan jumlah aktivitas
        base_score = min(len(activities) / 5, 1.0)  # Optimal 5 aktivitas per minggu
        return base_score
    
    def generate_insights(self, metrics: Dict, user_data: Dict) -> List[str]:
        """Generate insights berdasarkan metrics"""
        insights = []
        
        # Profile insights
        if metrics['profile_completion'] < 0.8:
            insights.append("Lengkapi profil Anda untuk rekomendasi yang lebih akurat")
        
        # Social insights
        if metrics['social_engagement'] < 0.5:
            insights.append("Bergabung dengan lebih banyak komunitas akan meningkatkan koneksi sosial")
        
        # Activity insights
        if metrics['activity_participation'] < 0.6:
            insights.append("Tambahkan lebih banyak aktivitas untuk gaya hidup yang lebih aktif")
        
        # Overall insights
        if metrics['overall_engagement'] >= 0.8:
            insights.append("Excellent! Anda sangat aktif di platform ini")
        elif metrics['overall_engagement'] >= 0.6:
            insights.append("Bagus! Anda cukup aktif, terus pertahankan")
        else:
            insights.append("Mari tingkatkan aktivitas Anda di platform ini")
        
        return insights

# Utility functions yang bisa digunakan langsung

def format_time_ago(timestamp_str: str) -> str:
    """Format waktu relatif (contoh: '2 hari yang lalu')"""
    try:
        timestamp = time.mktime(time.strptime(timestamp_str, "%Y-%m-%d"))
        now = time.time()
        diff = now - timestamp
        
        days = int(diff // 86400)
        if days == 0:
            return "Hari ini"
        elif days == 1:
            return "Kemarin"
        elif days < 7:
            return f"{days} hari yang lalu"
        elif days < 30:
            weeks = days // 7
            return f"{weeks} minggu yang lalu"
        else:
            months = days // 30
            return f"{months} bulan yang lalu"
    except:
        return "Waktu tidak diketahui"

def generate_activity_id() -> str:
    """Generate unique activity ID"""
    timestamp = int(time.time())
    random_part = random.randint(1000, 9999)
    return f"ACT_{timestamp}_{random_part}"

def generate_community_id() -> str:
    """Generate unique community ID"""
    timestamp = int(time.time())
    random_part = random.randint(1000, 9999)
    return f"COM_{timestamp}_{random_part}"

def generate_user_id() -> str:
    """Generate unique user ID"""
    timestamp = int(time.time())
    random_part = random.randint(1000, 9999)
    return f"USR_{timestamp}_{random_part}"

def clean_user_input(input_str: str) -> str:
    """Bersihkan input user dari karakter yang tidak diinginkan"""
    if not input_str:
        return ""
    
    # Remove leading/trailing whitespace
    cleaned = input_str.strip()
    
    # Remove multiple spaces
    cleaned = ' '.join(cleaned.split())
    
    # Remove potentially harmful characters
    harmful_chars = ['<', '>', '{', '}', '[', ']', '&', '|', ';']
    for char in harmful_chars:
        cleaned = cleaned.replace(char, '')
    
    return cleaned

def is_senior_friendly_time(time_str: str) -> bool:
    """Cek apakah waktu ramah untuk senior"""
    try:
        hour = int(time_str.split(':')[0])
        # Senior-friendly hours: 6AM to 6PM
        return 6 <= hour <= 18
    except:
        return True  # Default to True if can't parse

def calculate_age_from_birth_year(birth_year: int) -> int:
    """Hitung usia dari tahun lahir"""
    current_year = time.localtime().tm_year
    return current_year - birth_year

def format_indonesian_currency(amount: int) -> str:
    """Format mata uang Rupiah"""
    if amount == 0:
        return "Gratis"
    
    # Format with thousands separator
    formatted = f"Rp {amount:,}".replace(',', '.')
    return formatted

def extract_price_from_string(price_str: str) -> int:
    """Extract numeric price from string"""
    if not price_str or price_str.lower() == 'gratis':
        return 0
    
    try:
        # Extract digits only
        numeric_part = ''.join(filter(str.isdigit, price_str))
        return int(numeric_part) if numeric_part else 0
    except:
        return 0

def validate_indonesian_phone(phone: str) -> bool:
    """Validasi nomor HP Indonesia"""
    if not phone:
        return False
    
    # Remove spaces and dashes
    clean_phone = phone.replace(' ', '').replace('-', '')
    
    # Indonesian phone patterns
    patterns = [
        r'^08\d{8,11},  # 08xxxxxxxxxx
        r'^\+628\d{8,11},  # +628xxxxxxxxxx
        r'^628\d{8,11},  # 628xxxxxxxxxx
    ]
    
    import re
    return any(re.match(pattern, clean_phone) for pattern in patterns)

def get_time_greeting() -> str:
    """Dapatkan sapaan berdasarkan waktu saat ini"""
    current_hour = time.localtime().tm_hour
    
    if 5 <= current_hour < 11:
        return "Selamat pagi"
    elif 11 <= current_hour < 15:
        return "Selamat siang"
    elif 15 <= current_hour < 18:
        return "Selamat sore"
    else:
        return "Selamat malam"

def calculate_similarity_score(text1: str, text2: str) -> float:
    """Hitung similarity score antara 2 text (simple version)"""
    if not text1 or not text2:
        return 0.0
    
    text1_words = set(text1.lower().split())
    text2_words = set(text2.lower().split())
    
    intersection = text1_words.intersection(text2_words)
    union = text1_words.union(text2_words)
    
    if not union:
        return 0.0
    
    return len(intersection) / len(union)

def get_activity_emoji_by_category(category: str) -> str:
    """Dapatkan emoji berdasarkan kategori aktivitas"""
    emoji_map = {
        'olahraga': '💪',
        'fitness': '🏃‍♂️',
        'hobi': '🎨',
        'hobby': '🎨', 
        'kreatif': '🎭',
        'creative': '🎭',
        'edukasi': '📚',
        'education': '📚',
        'kesehatan': '💚',
        'health': '💚',
        'sosial': '👥',
        'social': '👥'
    }
    
    return emoji_map.get(category.lower(), '🌟')

def suggest_related_interests(interest: str) -> List[str]:
    """Suggest related interests berdasarkan satu interest"""
    
    related_map = {
        'berkebun': ['memasak', 'jalan kaki', 'fotografi'],
        'memasak': ['berkebun', 'crafting', 'berkumpul dengan keluarga'],
        'yoga': ['jalan kaki', 'olahraga ringan', 'meditasi'],
        'membaca': ['menulis', 'teknologi', 'bahasa asing'],
        'seni': ['crafting', 'fotografi', 'musik'],
        'teknologi': ['membaca', 'bahasa asing', 'fotografi'],
        'musik': ['seni', 'crafting', 'menonton film'],
        'jalan kaki': ['yoga', 'berkebun', 'fotografi']
    }
    
    return related_map.get(interest.lower(), [])

def generate_welcome_message(name: str, interests: List[str]) -> str:
    """Generate welcome message yang personal"""
    greeting = get_time_greeting()
    
    if not interests:
        return f"{greeting}, {name}! Selamat bergabung di SilverConnect."
    
    primary_interest = interests[0] if interests else "aktivitas"
    
    templates = [
        f"{greeting}, {name}! Senang melihat Anda tertarik dengan {primary_interest}.",
        f"{greeting}, {name}! SilverConnect memiliki banyak aktivitas {primary_interest} yang menarik.",
        f"{greeting}, {name}! Mari jelajahi komunitas {primary_interest} di SilverConnect."
    ]
    
    return random.choice(templates)

def estimate_activity_duration(activity_name: str) -> str:
    """Estimasi durasi aktivitas berdasarkan nama"""
    
    duration_map = {
        'yoga': '60-90 menit',
        'masak': '2-3 jam',
        'jalan': '30-60 menit',
        'senam': '45-60 menit',
        'lukis': '90-120 menit',
        'workshop': '2-4 jam',
        'diskusi': '60-90 menit',
        'belajar': '60-120 menit'
    }
    
    activity_lower = activity_name.lower()
    
    for keyword, duration in duration_map.items():
        if keyword in activity_lower:
            return duration
    
    return '60-90 menit'  # Default duration

def get_activity_difficulty_explanation(difficulty: str) -> str:
    """Penjelasan level kesulitan aktivitas"""
    
    explanations = {
        'mudah': 'Cocok untuk pemula, tidak memerlukan pengalaman khusus',
        'sedang': 'Memerlukan sedikit pengalaman atau stamina dasar', 
        'sulit': 'Untuk yang sudah berpengalaman dan memiliki stamina baik'
    }
    
    return explanations.get(difficulty.lower(), 'Level kesulitan tidak ditentukan')

def format_member_count(count: int) -> str:
    """Format jumlah anggota dengan text yang friendly"""
    if count == 0:
        return "Komunitas baru"
    elif count == 1:
        return "1 anggota"
    elif count < 10:
        return f"{count} anggota - komunitas kecil dan akrab"
    elif count < 25:
        return f"{count} anggota - ukuran ideal"
    elif count < 50:
        return f"{count} anggota - komunitas yang aktif"
    else:
        return f"{count} anggota - komunitas besar dan ramai"