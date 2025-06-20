import React, { useState, useEffect } from 'react';
import ProfileService from '../../services/ProfileService'; 
import { useParams } from 'react-router-dom';

import ProfileHeader from './ProfileHeader';
import PostList from './PostList';
import ConnectionList from './ConnectionList';
import LoadingSpinner from '../../components/LoadingSpinner';

function UserProfileScreen() {
  const { userId } = useParams(); 
  const [profileData, setProfileData] = useState(null);
  const [isLoading, setIsLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchProfile = async () => {
      try {
        setIsLoading(true);
        const data = await ProfileService.getProfilePageData(userId);
        setProfileData(data);
        // -----------------------------
      } catch (err) {
        setError('Gagal memuat profil, silakan coba lagi nanti.');
        console.error(err);
      } finally {
        setIsLoading(false);
      }
    };

    fetchProfile();
  }, [userId]); 

  if (isLoading) {
    return <LoadingSpinner />;
  }

  if (error) {
    return <div className="error-message">{error}</div>;
  }

  return (
    <div className="profile-page">
      {profileData && (
        <>
          <ProfileHeader user={profileData.userDetails} />
          <ConnectionList connections={profileData.connections} />
          <PostList posts={profileData.posts} />
        </>
      )}
    </div>
  );
}

export default UserProfileScreen;